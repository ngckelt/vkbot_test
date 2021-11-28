
$(document).ready(function () {
    // translateWeekDays();
    setupShowHomeworkBlock();
    setupChangeFormCloseButton();
    setupUpdateHomeworkButton();
});

function translateDay(text) {
    if (text.find("Monday")) {
        console.log(text);
    }
}

function translateWeekDays() {
    $(".homework-date").each(function () {
        text = $(this).text();
        translateDay(text);
        // console.log(text);
    });
}

function setupShowHomeworkBlock() {
    $(".show-homework-arrow").on('click', function () {
        arrow = $(this).children()[1];
        $(arrow).toggleClass('flipped');
        homeworkBlock = $($(this).siblings()[0]);
        toggleHomeworkDataDisplay(homeworkBlock);
    });
}

function toggleHomeworkDataDisplay(element) {
    if ($(element).attr('data-opened') == 'false') {
        $(element).css('height', $(element).prop('scrollHeight') + 10 + 'px');
        $(element).attr('data-opened', 'true');
    } else {
        $(element).attr('data-opened', 'false');
        $(element).css('height', '0');
    }
}


function setupChangeFormCloseButton() {
    $("#closeHomeworkChangeBlockCross").on('click', function () {
        $("#homeworkChangeBlock").css('display', 'none');
        $("#backgroundDisableBlock").css('display', 'none');
    });
}

function fillHomeworkChangeForm(subject, text, date, homework_id) {
    select = $("#updateHomeworkSubject");
    $(select).prepend("<option value=\""+subject+"\">"+ subject +"</option>");
    $("#updateHomeworkText").val(text);
    $("#updateHomeworkDate").val(date);
    $("#homeworkId").val(homework_id);
}

function setupUpdateHomeworkButton() {
    $(".update-homework").on('click', function () {
        $("#homeworkChangeBlock").css('display', 'block');
        $("#backgroundDisableBlock").css('display', 'block');
        homeworkData = $($(this).parent()).siblings();
        subject = $(homeworkData[0]).text();
        text = $(homeworkData[1]).val();
        date = $(homeworkData[2]).val();
        homeworkId = $(this).attr('data-homework-id');
        fillHomeworkChangeForm(subject, text, date, homeworkId);
    });
}


