var Popuper = function() {
    return {
        open : function(event) {
            var trigger = $(event.target);
            var leftPos = trigger.position().left;
            var topPos = trigger.position().top;
            $.ajax({
                url: event.target.href,
                success: function(html, status, jqXHR) {
                    $('#pageContent').append('<div class="popupForm" id="popupForm"></div>');
                    var popup = $('#popupForm');
                    popup.append(html);
                    $('#popupForm').css('top', topPos-popup.padding().top);
                    $('#popupForm').css('left', leftPos-popup.padding().left);
                }
            });
            return false;
        }
    };
}();

$(document).ready(function() {
    $('body').on('click', '.editOpener', Popuper.open);
});