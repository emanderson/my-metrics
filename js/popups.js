var Popuper = function() {
    return {
        open : function(event) {
            $.ajax({
                url: event.target.href,
                success: function(html) {
                    $('#pageContent').append(html);
                }
            });
            return false;
        }
    };
}();

$(document).ready(function() {
    $('body').on('click', '.editOpener', Popuper.open);
});