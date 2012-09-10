var Popuper = function() {
    return {
        open : function(event) {
            var trigger = $(event.target);
            var leftPos = trigger.position().left;
            var topPos = trigger.position().top;
            $.ajax({
                url: event.target.href,
                success: function(html, status, jqXHR) {
                    var pageContent = $('#pageContent');
                    pageContent.append('<div class="popupForm" id="popupForm"></div>');
                    var popup = $('#popupForm');
                    popup.append(html);
                    var top = topPos;
                    if (top + popup.height() > pageContent.height()) {
                        top = pageContent.height() + pageContent.position().top - popup.height();
                    }
                    popup.css('top', top-popup.padding().top);
                    popup.css('left', leftPos-popup.padding().left);
                    form = popup.find('form')[0];
                    popup.on('click', 'input[name=save]', function() {
                        $.ajax({
                            url: form.action,
                            type: form.method,
                            data: $(form).serialize(),
                            success: function(html) {
                                var oldOne = $('#' + $(html).attr('id'));
                                oldOne.replaceWith(html);
                                $("#popupForm").remove();
                            }
                        });
                        return false;
                    });
                }
            });
            return false;
        }
    };
}();

$(document).ready(function() {
    $('body').on('click', '.editOpener', Popuper.open);
});