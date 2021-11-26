(function ($) {
	$.fn.bindWithDelay = function (type, data, fn, timeout, throttle) {
		if ($.isFunction(data)) {
			throttle = timeout;
			timeout = fn;
			fn = data;
			data = undefined;
		}
		fn.guid = fn.guid || ($.guid && $.guid++);
		return this.each(function () {
			var wait = null;
			function cb() {
				var e = $.extend(true, {}, arguments[0]);
				var ctx = this;
				var throttler = function () {
					wait = null;
					fn.apply(ctx, [e]);
				};
				if (!throttle) {
					clearTimeout(wait);
					wait = null;
				}
				if (!wait) {
					wait = setTimeout(throttler, timeout);
				}
			}
			cb.guid = fn.guid;
			$(this).bind(type, data, cb);
		});
	};
})(jQuery);

function isMobile() { 
    return (navigator.userAgent.match(/Android/i)
        || navigator.userAgent.match(/webOS/i)
        || navigator.userAgent.match(/iPhone/i)
        || navigator.userAgent.match(/iPad/i)
        || navigator.userAgent.match(/iPod/i)
        || navigator.userAgent.match(/BlackBerry/i)
        || navigator.userAgent.match(/Windows Phone/i)
    );
}

function getVH() {
    var vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', vh + 'px');
}

getVH();

(function ($) {
	$.fn.tabs = function (options) {
		options = $.extend({}, $.fn.tabs.options, options);

		return $(this).each(function () {
			var $tabs = $(this);
			$(options.tabSelectorLink, $tabs).on('click', function (e) {
				e.preventDefault();
				var $this = $(this);
				if (!$this.hasClass(options.activeClass)) {
					$(options.tabSelectorLink, $tabs).removeClass(options.activeClass);
					$this.addClass(options.activeClass);
					$(options.tabSelectorContent, $tabs).removeClass('is-active');
					var $tabContent = $($this.attr('href'), $tabs);
					$tabContent.addClass('is-active');
					if (typeof options.afterShow === 'function') {
						options.afterShow($this, $tabContent, $tabs);
					}
				}
			}).eq(options.tabInitIndex).trigger('click');
		});
	};
	$.fn.tabs.options = {
		activeClass: 'is-active',
		tabSelectorLink: '.js-tabs-link',
		tabSelectorContent: '.js-tabs-content',
		tabInitIndex: 0,
		afterShow: null
	};
})(jQuery);

(function ($) {
	$.fn.accordion = function (options) {
		options = $.extend({}, $.fn.accordion.options, options);

		var hash = window.location.hash;
		if (typeof hash !== 'undefined' && hash.length > 0) {
			$(options.accondionSelectorLink + '[href="' + hash + '"]').trigger('click');
		}

		return $(this).each(function () {
			var $accordion = $(this);
			var multiply = (typeof $accordion.data('multiply') !== 'undefined');
			var notOpenFirst = (typeof $accordion.data('notOpenFirst') !== 'undefined');
			var $links = $(options.accondionSelectorLink, $accordion);

			$links.on('click', function (e) {
				e.preventDefault();
				var $this = $(this);
				var $accordionContent = $this.nextAll(options.accordionSelectorContent).eq(0);
				if (multiply) {
					if (!$this.hasClass(options.activeClass)) {
						$this.addClass(options.activeClass);
						$accordionContent.slideDown(300, function () {
							if (typeof options.afterShow === 'function') {
								options.afterShow($this, $accordionContent, $accordion);
							}
						});
					} else {
						$this.removeClass(options.activeClass);
						$accordionContent.slideUp(300);
					}
				} else {
					if (!$this.hasClass(options.activeClass)) {
						$links.removeClass(options.activeClass);
						$this.addClass(options.activeClass);
						$(options.accordionSelectorContent, $accordion).slideUp(300);
						$accordionContent.slideDown(300, function () {
							if (typeof options.afterShow === 'function') {
								options.afterShow($this, $accordionContent, $accordion);
							}
						});
					}
				}
			});
			if (!notOpenFirst) {
				$links.eq(0).trigger('click');
			}
		});
	};
	$.fn.accordion.options = {
		activeClass: 'is-active',
		accondionSelectorLink: '.js-accordion-link',
		accordionSelectorContent: '.js-accordion-content',
		afterShow: null
	};
})(jQuery);
	
(function ($, document) {
    $.fn.popup = function (options) {
        options = $.extend({}, $.fn.popup.options, options);
        var $body = $('body');
        var $document = $(document);
        var $oldPopup = $('.popup');
        var scrollbarWidth = getScrollbarWidth();
        var isBodyOverflowing = document.body.clientWidth < window.outerWidth;

        function getScrollbarWidth() {
            var scrollDiv = document.createElement('div');
            scrollDiv.className = 'popup-scrollbar-measure';
            document.body.appendChild(scrollDiv);
            var scrollbarWidth = scrollDiv.getBoundingClientRect().width - scrollDiv.clientWidth;
            document.body.removeChild(scrollDiv);
            return scrollbarWidth;
        }

        function closeByEsc(e) {
            if (Number(e.keyCode) === 27) {
                $('.popup').trigger('click', {'close': true});
            }
        }

        $document.on('showPopup', function (e, params) {
			var $popup = $('#' + params.$link.data('popupId'));
            var $popupContainer = $popup.find('.popup__container');

            if ($popup.length <= 0) {
                return;
            }

            if ($oldPopup.is(':visible')) {
                $body.removeClass(options.bodyClassName);
                $oldPopup.off('click').hide();
            } else {
                if (isBodyOverflowing) {
                    var actualPadding = document.body.style.paddingRight;
                    var calculatedPadding = $body.css('padding-right');
                    $body.data('padding-right', actualPadding).css('padding-right', parseFloat(calculatedPadding) + scrollbarWidth + 'px');
                }
            }

            if (typeof options.beforeShow === 'function') {
                options.beforeShow($popup, params.$link);
            }

            $popup.show();
            $popupContainer.addClass(options.animateClassName).scrollTop(0);
            $body.addClass(options.bodyClassName);

            setTimeout(function () {
                $popupContainer.removeClass(options.animateClassName);
                if (typeof options.afterShow === 'function') {
                    options.afterShow($popup, params.$link);
                }
            }, 300);

            $document.on('keyup', closeByEsc);

            $popup.on('click', function (e, p = {'close': false}) {
                var $target = $(e.target);
                if ($target.hasClass('popup__close') ||
                    $target.parents('.popup__close').length ||
                    (!$target.hasClass('popup__content') && !$target.parents('.popup__content').length && ($popup.data('modal') === undefined || p.close))
                ) {
                    e.preventDefault();
                    var padding = $body.data('padding-right');
                    $popup.off('click').fadeOut(100, function () {
                        if (typeof padding !== 'undefined') {
                            $body.css('padding-right', padding).removeData('padding-right');
                        }
                        $body.removeClass(options.bodyClassName);
                        if (typeof options.afterHide === 'function') {
                            options.afterHide($popup, params.$link);
                        }
                    });
                    $document.off('keyup', closeByEsc);
                }
            });
        });

        $document.on('click', '[data-popup-id]', function (e) {
            var $link = $(this);
            var prevent = (typeof $link.data('prevent') === 'undefined');
            var url = (typeof $link.data('url') !== 'undefined'); // для динамической подгрузки содержимого
            if (prevent) {
                e.preventDefault();
            }	
			if (url) {
				// цель - либо .popup__dynamic-content, сохраняем заголовок "окошка" 
				var placeholder = $('.popup__dynamic-content, .popup__wrapper', $('#' + $link.data('popupId'))).last(); 
				$.get($link.data('url'), function (result) {
					$(placeholder).html(result);
				}).done(function(){
					$document.trigger('showPopup', {
						$link: $link
					});
				});
			}
			else {
				$document.trigger('showPopup', {
					$link: $link
				});
			}	
        });
    };

    $.fn.popup.options = {
        animateClassName: 'animation-target',
        bodyClassName: 'body-fixed',
        beforeShow: null,
        afterShow: null,
        afterHide: null
    };

})(jQuery, document);

(function ($, document) {
    $.fn.tableResponse = function (options) {
        options = $.extend({}, $.fn.tableResponse.options, options);
        var $window = $(window);
        var offset = 20;

        function showScroll($this) {
            var _this = $this.find('.table-responsive__wrapper').get(0);
            if(_this.scrollWidth > _this.clientWidth) {
                $this.addClass('is-scroll-show');
            } else {
                $this.removeClass('is-scroll-show');
            }
        }


        function initScroll($this) {
            var _this = $this.find('.table-responsive__wrapper').get(0);
            $this.removeClass('is-right-end is-left-end');
            if (_this.offsetWidth + _this.scrollLeft >= (_this.scrollWidth - offset)) {
                $this.addClass('is-right-end');
            } else if (_this.scrollLeft <= offset) {
                $this.addClass('is-left-end');
            }
        }

        return $(this).each(function () {
            var $this = $(this);

            $this.wrapInner('<div class="table-responsive__wrapper"/>');
            $('<div class="table-responsive__swipe _to-left"/>').prependTo($this);
            $('<div class="table-responsive__swipe _to-right">' +
                '<svg class="svg-swipe-icon" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">' +
                '<use xlink:href="#swipe-icon"></use>' +
                '</svg></div>').appendTo($this);

            showScroll($this);
            initScroll($this);

            $window.on('resize', function () {
                showScroll($this);
            });

            $this.find('.table-responsive__wrapper').on('scroll', function (e) {
                initScroll($this);
            });		
			
			if ($this.hasClass('table--hidden')) {
				$this.hide();
			}
        });
    };

    $.fn.tableResponse.options = {
    };
})(jQuery, document);

$(function () {			
    $(document).on('loadMoreMainEvents', function (e, params) {       
        $.getJSON(params.url, function (result) {
            params.callback();
            params.callbackSuccess(result);
        }, 'json');
    }).on('loadMoreCalendarEvents', function (e, params) {        
        /**
         * params.lastDay - последний выданный день
         * params.query - строка поискового запроса
         * params.cleanQuery - когда поле отчистили, отдается true, в остальных случая всегда false
         */      
        $.getJSON(params.url, {"lastDay": params.lastDay, "query": params.query, "cleanQuery": params.cleanQuery}, function (result) {
            params.callback();
            params.callbackSuccess(result);
        }, 'json');
    }).on('scheduleSearch', function (e, params) {
        $.getJSON(params.url, {"query" : params.query}, function (result) {
            params.callback();
            params.callbackSuccess(result);
        }, 'json');
    }).on('loadMoreEvents', function (e, params) {				
        $.getJSON(params.url, {"content_type": params.contentType, "content_filter": params.contentFilter, "last_item": params.lastItem}, function (result) {
            params.callback();
            params.callbackSuccess(result);
        }, 'json');
    }).on('showHideItems', function (e, params) {
        params.callback();
        params.$btn.remove();
        params.$target.removeClass('is-hide');
    }).on('eduSystemsTable', function (e, params) {
        $.get(params.url+'&'+params.data, function (result) {
            params.callbackSuccess(result);
        }, 'html')
    }).on('priceTable', function (e, params) {
        $.get(params.url, function (result) {
            setTimeout(function () {
                params.callbackSuccess(result);
            }, 500);
        }, 'html')
    }).on('loadMoreScienceEvents', function (e, params) {
        $.getJSON(params.url+'&'+params.data, function (result) {
            params.callback();
            params.callbackSuccess(result);
        }, 'json');
    });  

	/**
	 * Быстрые ссылки
	 */	
	$(function () {
		(function ($contentMenu) {
			if (!$contentMenu.length) {
				return;
			}

			var offset = 20;
			var $wrapper = $('.content-menu__wrapper', $contentMenu);

			initScroll();

			$wrapper.on('scroll', function (e) {
				initScroll();
			});

			function initScroll() {
				var _this = $wrapper.get(0);
				$contentMenu.removeClass('is-right-end is-left-end');
				if (_this.offsetWidth + _this.scrollLeft >= (_this.scrollWidth - offset)) {
					$contentMenu.addClass('is-right-end');
				} else if (_this.scrollLeft <= offset) {
					$contentMenu.addClass('is-left-end');
				}
			}
		})($('.content-menu'));
	});

	/**
	 * Анимирование элементов шапки
	 */
    (function ($header) {
        if (!$header.length) {
            return;
        }
        var bindDelay = 300;
        var showMenuTimer;
        $('.js-header-menu-item', $header).on('mouseenter', function (e) {
            var $this = $(this);
            showMenuTimer = setTimeout(function () {
                $this.addClass('is-hover');
            }, bindDelay);
        }).on('mouseleave', function (e) {
            var $this = $(this);
            if (showMenuTimer) {
                clearTimeout(showMenuTimer);
                showMenuTimer = null;
            }
            $this.removeClass('is-hover');
        });
    })($('.page-header'));
	
	/**
	 *	Поиск по сайту
	 */
    (function ($headerSearch) {
        if (!$headerSearch.length) {
            return;
        }
        var $headerSearchBtn = $('.js-header-search-btn');

        $headerSearchBtn.on('click', function (e) {
            e.preventDefault();
            if ($headerSearch.hasClass('is-open')) {
                $headerSearch.removeClass('is-open');
                $headerSearchBtn.removeClass('is-open');
            } else {
                $headerSearch.addClass('is-open').find('input').focus();
                $headerSearchBtn.addClass('is-open');
            }
        });
    })($('.header-search'));
	
	/**
	 *	Шапка адаптивной версии
	 */
    (function ($headerMobile) {
        if (!$headerMobile.length) {
            return;
        }
        var $body = $('body');

        $('.js-header-mobile-burger', $headerMobile).on('click', function (e) {
            e.preventDefault();
            if ($body.hasClass('is-open-menu')) {
                if($body.hasClass('is-open-menu-login')) {
                    $body.removeClass('is-open-menu-login').scrollTop(0);
                }
				else if ($body.hasClass('is-open-menu-ask')) {
                    $body.removeClass('is-open-menu-ask').scrollTop(0);
                }
				else {
                    $body.removeClass('is-open-menu');
                }
            } else {
                $body.addClass('is-open-menu').scrollTop(0);
            }
        });
    })($('.header-mobile'));
	
	/**
	 *	Интерактивные элементы шапки мобильной версии: вход, меню
	 */
    (function ($headerSidebar) {
        if (!$headerSidebar.length) {
            return;
        }
        var $body = $('body');

        $('.js-header-mobile-login', $headerSidebar).on('click', function (e) {
            e.preventDefault();
            $body.addClass('is-open-menu-login').scrollTop(0);
        });         
		$('.js-header-mobile-ask', $headerSidebar).on('click', function (e) {
            e.preventDefault();
            $body.addClass('is-open-menu-ask').scrollTop(0);
        });        

        $('.js-header-sidebar-trigger', $headerSidebar).on('click', function (e) {
            e.preventDefault();
            var $this = $(this);
            var $parent = $this.parents('.js-header-sidebar-item');
            if($parent.hasClass('is-open')) {
                $parent.removeClass('is-open')
            } else {
                $parent.addClass('is-open')
            }
        });
    })($('.header-sidebar'));
	/**
	 * Индикатор загрузки
	 */	
	(function ($loader) {
        if (!$loader.length) {
            return;
        }

        $(document).ajaxStart(function () {
            $loader.show();
			//$loader.addClass('is-show');
        }).ajaxStop(function () {
			$loader.hide();
            //$loader.removeClass('is-show');
        });
    })($('.loader'));

	/**
	 * Кнопка "Вверх"
	 */		
    (function ($toTop) {
        if (!$toTop.length) {
            return;
        }
        var $window = $(window);
        var windowHeight = $window.height();

        $window.scroll(function (e) {
            var scroll = $window.scrollTop();
            if (scroll >= windowHeight) {
                $toTop.addClass('is-show');
            } else {
                $toTop.removeClass('is-show');
            }
        }).on('resize', function () {
            windowHeight = $window.height();
        });

        $toTop.on('click', function (e) {
            e.preventDefault();
            var $selector = $('.page-header');
            if ($selector.length) {
                var targetTop = $selector.offset().top;
                $('html, body').animate({
                    scrollTop: targetTop
                }, {
                    queue: false,
                    duration: 150
                });
            }
        });
    })($('.to-top'));	
	/**
	 * "Показать ещё" для виджетов
	 */
    (function ($loadMore) {
        if (!$loadMore.length) {
            return;
        }

        $loadMore.on('click', function (e) {
            e.preventDefault();
            var $this = $(this);
            var $target = $($this.data('target'));
            var url = $this.data('url');          
            var contentType = $target.data('contentType');          
            var contentFilter = $target.data('contentFilter');          
            var lastItem = $this.data('lastItem');          
            var callback = $this.data('callback');
            if(!$target.length || typeof callback === "undefined") {
                return;
            }
            if ($this.hasClass('is-loading')) {
                return;
            }
            $this.addClass('is-loading');
            if (typeof url !== "undefined") {
                $(document).trigger(callback, {
                    $btn: $this,
                    $target: $target,
                    url: url,
                    contentType: contentType,
                    contentFilter: contentFilter,
					lastItem:  lastItem,				
                    callback: function () {
                        $this.removeClass('is-loading');
                    },
                    callbackSuccess: function (result) {
						$this.data('lastItem', result.lastItem);
                        if (Boolean(result.haveMore) === false)                           
                            $this.remove();                        
                        if (result.items && result.items.length) {
                            var itemsHtml = result.items;
                            $(itemsHtml).appendTo($target);
                        }
                    }
                });
            } else {
                $(document).trigger(callback, {
                    $btn: $this,
                    $target: $target,
                    callback: function () {
                        $this.removeClass('is-loading');
                    }
                });
            }
        });
    })($('.load-more'));
	
	/**
	 *	Промо-блок на главной странице
	 */
	(function ($mainPromo) {
		if (!$mainPromo.length) {
			return;
		}

		$mainPromo.each(function () {
			var $slider = $(this);
			var $slides = $('.js-slides', $slider);

			$slides.slick({
				infinite: true,
				autoplay: true,
				slidesToShow: 1,
				slidesToScroll: 1,
				dots: true,
				arrows: false,
				rows: 0
			});
		});
	})($('.main-promo'));

	/**
	 * Подгрузка событий из жизни увиверситета
	 */ 	 
	(function ($mainEvents) {
		if (!$mainEvents.length) {
			return;
		}
		loadGif();

        $(document).on('mainEventsLoadGif', function () {
            loadGif();
        });

        function loadGif() {
            if (isMobile()) {
                return;
            }
            $('.main-events__item', $mainEvents).each(function () {
                var $this = $(this);
                var gif = $this.attr('data-gif');
                if (typeof gif !== "undefined") {
                    $this.css('background-image', 'url("' + gif + '")').removeAttr('data-gif');
                }
            })
        }
		
		var $grid = $('.js-main-events-grid', $mainEvents);
		$('.main-events__more', $mainEvents).on('click', function (e) {
			e.preventDefault();
			var $this = $(this);
			if ($this.hasClass('is-loading')) {
				return;
			}
			$this.addClass('is-loading');
			$(document).trigger('loadMoreMainEvents', {
				$link: $this,
				url: $this.data('url'),
				callback: function () {
					$this.removeClass('is-loading');
				},
				callbackSuccess: function (result) {
					if (Boolean(result.haveMore) === true) {
						$this.data('url', result.nextUrl);
					} else {
						$this.remove();
					}
					if (result.items && result.items.length) {
						var itemsHtml = result.items;
						$(itemsHtml).appendTo($grid);
						loadGif();
					}
				}
			});
		});
	})($('.main-events'));
	

	/**
	 *	Подгрузка событий в календарь на главной странице
	 */
	(function ($calendarEvents) {
        if (!$calendarEvents.length) {
            return;
        }

        var $days = $('.js-calendar-events-days', $calendarEvents);
        var $input = $('.js-calendar-events-search', $calendarEvents);
        var $more = $('.js-calendar-events-more', $calendarEvents);

        $days.on('scroll', scroll);

        $input.bindWithDelay('input', function () {
            loadData(true, Boolean($input.val() === ''));
        }, 300);

        $more.on('click', function (e) {
            e.preventDefault();
            var $hideEvents = $calendarEvents.data('hideEvents');
			//console.log($hideEvents);
            if($hideEvents  && $hideEvents.length > 0) {
                $hideEvents.appendTo($days);
                $calendarEvents.data('hideEvents', null);
            } else {
                loadData();
            }
        });
		
		function scroll(e) {
			e.preventDefault();
			e.stopPropagation();
			var element = e.currentTarget;
			//console.log(element.scrollHeight+' - '+element.scrollTop+' - '+element.clientHeight)
			if ((element.scrollHeight - element.scrollTop - 1 < element.clientHeight) && $input.val() === '') {
				loadData();
			}
		}
		function loadData(refresh, emptyQ) {
			refresh = refresh || false;
			emptyQ = emptyQ || false;
			if ($days.hasClass('is-loading')) {
				return;
			}
			$days.addClass('is-loading');
			$(document).trigger('loadMoreCalendarEvents', {
				url: $days.data('url'),
				lastDay: $days.data('lastDay'),
				query: $input.val(),
				cleanQuery: emptyQ,
				haveMore: $days.data('haveMore'),
				callback: function () {
					$days.removeClass('is-loading');
				},
				callbackSuccess: function (result) {         
					$days.data('lastDay', result.lastDay);
					$days.data('haveMore', Boolean(result.haveMore));                             
					if (Boolean(result.haveMore) === true) {
						$days.on('scroll', scroll);
						$more.removeClass('is-hide');
					} else {
						$days.off('scroll', scroll);                       
						$more.addClass('is-hide');
					}
					if (result.days && result.days.length) {
						var itemsHtml = result.days; 
						if(refresh) {
							$days.html(itemsHtml).scrollTop(0);
						} else {
							$(itemsHtml).appendTo($days);
						}
					}
					else if ($input.val()) $days.html('').scrollTop(0);
				}
			});
		}
    })($('.calendar-events'));
	
	
	/**
	 * Промо видео
	 */
	(function ($promoVideo) {
		if (!$promoVideo.length) {
			return;
		}
		var $window = $(window);
		var $screen = $('.js-promo-video-screen', $promoVideo);
		var $btn = $('.js-promo-video-btn', $promoVideo);	
		var video = $screen.get(0);		
		screenResize();

		$btn.on('click', function (e) {
			e.preventDefault();
			$promoVideo.addClass('is-play');
			video.play();
		});

		$window.on('resize', function () {
			screenResize();
		});

		function screenResize() {
			var w = $window.width(),
			h = $window.height();
			if (w / h > 16 / 9) {
				$screen.css({width: w, height: (w / 16 * 9)});
			} else {
				$screen.css({width: '100%', height: '100%'});
			}
		}
	})($('.promo__video'));
	
	var $window = $(window);
    var $document = $(document);
	var $body = $('body');
	
	$window.on('resize orientationchange', function () {
		getVH();
	});

    $('.js-tabs').tabs();
    $('.js-accordion').accordion();
	$('.table-responsive').tableResponse();
	
	$('[data-popup-id]').popup({
        afterShow: function ($popup) {
            var $form = $popup.find('form');
            if ($form.length) {
                $form.find('input').eq(0).focus();
            }
        },
        afterHide: function ($popup) {
            $popup.find('iframe').each(function () {
                var $this = $(this);
                $this.attr('src', $this.attr('src'));
            });
        }
    });
	
	(function ($select) {
        if (!$select.length) {
            return
        }

        $select.each(function () {
            var $this = $(this);
            $this.selectric({
                responsive: true
            });
        });
    })($('.js-select'));

	/**
	 * Автокомплит
	 */	
	(function ($suggest) {
        if (!$suggest.length) {
            return
        }

        $suggest.each(function () {
            var $this = $(this);
            var $input = $('.js-suggest-input', $this);
            var $result = $('.js-suggest-result', $this);
            var url = $this.data('url');

            $input.on('input', function () {     
                var $_this = $(this);
                var value = $.trim($_this.val());
                var minlength = parseInt($_this.attr('minlength'), 10);
                minlength = minlength || 2;
                if (value.length >= minlength) {
                    $.get(url, {term: value}, function (result) {        
                        $result.html(result).addClass('is-open');
                    }, 'json')
                } else {
                    $result.html('').removeClass('is-open');     
                }
            });
        });
		$suggest.on('mouseenter', '.form-suggest__result-item', function () {
            var $item = $(this);
            var $parent = $item.parents('.js-suggest');
            var $input = $('.js-suggest-input', $parent);
            $input.val($.trim($item.text()));
        });

        $document.on('click', function (e) {
            var $target = $(e.target);
            if (
                !$target.hasClass('js-suggest') &&
                !$target.parents('.js-suggest').length
            ) {
                $('.js-suggest-result').html('').removeClass('is-open');
            }
        })
    })($('.js-suggest'));
	
    $('.js-video-btn').on('click', function (e) {
        e.preventDefault();
        var $this = $(this);
        var $parent = $this.parents('.js-video');
        $parent.addClass('is-play');
        $parent.find('video').get(0).play();
    });

	/**
	 *	Для мобильной версии: перемещение блока с календарем событий в нужное место 
	 */
	(function ($mainPage) {
		if(!$mainPage.length) {
			return;
		}

		var $window = $(window);
		var $document = $(document);
		var $body = $('body');
		var hideCalendarEvents = false;
        var $calendarEvents = $('.calendar-events');

        moveAside();

        $window.on('resize orientationchange', function () {
            moveAside();
        });

        function moveAside() {
            var needMove = (window.matchMedia('(max-width: 1000px)').matches);
            var isMoving = $body.hasClass('is-aside-moving');
            // Если нужно перемещать и еще не перемещали, то перемещаем
            if (needMove && !isMoving) {
                $body.addClass('is-aside-moving');
                $('.page-aside').contents().appendTo($('.js-main-aside-mobile'));
                if (!hideCalendarEvents) {
                    hideCalendarEvents = true;
                    var $events = $('.calendar-events__days-item').not(':first-child');
                    $calendarEvents.data('hideEvents', $events);
                    $events.remove();
                }
            }
            // Если не нужно перемещать и уже перемещали, то возвращаем обратно
            if (!needMove && isMoving) {
                $body.removeClass('is-aside-moving');
                $('.js-main-aside-mobile').contents().appendTo($('.page-aside'));
                if (hideCalendarEvents) {
                var $hideEvents = $calendarEvents.data('hideEvents');
                    $hideEvents.appendTo($('.js-calendar-events-days', $calendarEvents));
                    $calendarEvents.data('hideEvents', null);
                }
            }
        }
	})($('.main-page'));
});