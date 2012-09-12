var CalorieGrapher = function() {
    var AXES_HEIGHT = 390;
    var AXES_WIDTH = 790;
    var AXES_OFFSET = 10;
    var MAX_BAR_HEIGHT = 380;
    var BAR_WIDTH = 35;
    var BAR_SPACE = 15;

    function drawAxes() {
        var canvas = document.getElementById('calorieGraph');
        if (canvas.getContext) {
            var context = canvas.getContext('2d');
            context.strokeColor = '#000000';
            context.moveTo(AXES_OFFSET, AXES_OFFSET);
            context.lineTo(AXES_OFFSET, AXES_HEIGHT);
            context.lineTo(AXES_WIDTH, AXES_HEIGHT);
            context.stroke();
        } else {
            console.log('No canvas support');
        }    
    };
    
    var barColors = [
        '#474ff4',
        '#f447d8',
        '#dc6740',
        '#c39d39',
        '#b0c339',
        '#3cd0aa',
        '#9947f4',
        '#f4475d',
        '#c38139',
        '#c3b939',
        '#5ec339'
    ];
    var lastColor = 0;
    
    var bars = [];
    var tags = [];
    var tag_colors = {};
    
    function drawBarPart(context, left, top, right, bottom, color) {
        if (typeof color === 'undefined') {
            color = barColors[lastColor];
            lastColor = (lastColor + 1) % barColors.length;
        }
        context.fillStyle = color;
        context.strokeColor = color;
        context.beginPath()
        context.moveTo(left, top);
        context.lineTo(left, bottom);
        context.lineTo(right, bottom);
        context.lineTo(right, top);
        context.closePath();
        context.fill();
    };
    
    function drawBar(dayData, maxBarPercent, barPosition, mode) {
        mode = typeof mode !== 'undefined' ? mode : 'entries';
        var barLeft = barPosition * (BAR_WIDTH + BAR_SPACE) + BAR_SPACE + AXES_OFFSET;
        var barHeight = maxBarPercent * MAX_BAR_HEIGHT;
        var canvas = document.getElementById('calorieGraph');
        var bar = {
            left: barLeft,
            top: AXES_HEIGHT-barHeight,
            right: barLeft + BAR_SPACE * 2,
            bottom: AXES_HEIGHT,
            day: dayData
        };
        if (canvas.getContext) {
            var context = canvas.getContext('2d');
            var bottom = bar.bottom;
            var top = bar.bottom;
            var height = 0;
            if (mode === 'entries') {
                for (var i=0; i<bar.day.entries.length; i++) {
                    var entry = bar.day.entries[i];
                    height = entry.calories/bar.day.total_calories*barHeight;
                    top -= height;
                    drawBarPart(context, bar.left, top, bar.right, bottom);
                    bars.push({
                        left: bar.left,
                        top: top,
                        right: bar.right,
                        bottom: bottom,
                        day: bar.day,
                        entry: entry
                    });
                    bottom -= height;
                }
            } else if (mode === 'tags') {
                for (var i=0; i<tags.length; i++) {
                    var tag_id = tags[i].id;
                    var entries_for_tag = bar.day.by_tag[tag_id];
                    if (entries_for_tag !== undefined) {
                        var tag_calories = 0;
                        for (var j=0; j<entries_for_tag.length; j++) {
                            tag_calories += entries_for_tag[j].calories;
                        }
                        height = tag_calories/bar.day.total_calories*barHeight;
                        top -= height;
                        drawBarPart(context, bar.left, top, bar.right, bottom, tag_colors[tag_id]);
                        bars.push({
                            left: bar.left,
                            top: top,
                            right: bar.right,
                            bottom: bottom,
                            day: bar.day,
                            entry: {
                                calories: tag_calories,
                                name: tags[i].name
                            }
                        });
                        bottom -= height;
                    }
                }
            }
        } else {
            console.log('No canvas support');
        }    
    };
    
    function drawFetchedData(data) {
        for (var i=0; i<data.tags.length; i++) {
            tags.push(data.tags[i]);
            tag_colors[data.tags[i].id] = barColors[i%barColors.length];
        }
    
        var topCalories = 0;
        for (var i=0; i<data.food_days.length; i++) {
            var day = data.food_days[i];
            var calories = day.total_calories;
            if (topCalories < calories) {
                topCalories = calories;
            }
        }
        for (var i=0; i<data.food_days.length; i++) {
            var day = data.food_days[i];
            var calories = day.total_calories;
            drawBar(day, calories/topCalories, i, 'tags');
        }
    };
    
    function drawData() {
        $.ajax({
            url: '/graph/data',
            dataType: 'json',
            success: drawFetchedData
        });
    };
    
    var mouseOver = null;
    
    function barAt(xCoord, yCoord) {
        for (var i=0; i<bars.length; i++) {
            var bar = bars[i];
            if (xCoord >= bar.left && xCoord <= bar.right &&
                yCoord >= bar.top && yCoord <= bar.bottom) {
                return bar;
            }
        }
        return null;
    };
    
    function showMouseOverForBar(bar, event) {
        if (!mouseOver) {
            $('#pageContent').append('<div id="graphMouseOver" class="graphMouseOver"></div>');
            mouseOver = $('#graphMouseOver');
        }
        //mouseOver.text(bar.day.date + ': ' + bar.day.total_calories);
        mouseOver.html('<p>' + bar.day.date + '</p>' + 
            '<p>' + bar.entry.name + ': ' + bar.entry.calories + '</p>');
        mouseOver.css('left', event.pageX);
        mouseOver.css('top', event.pageY);
        mouseOver.show();
    };
    
    function hideMouseOver() {
        if (mouseOver) {
            mouseOver.hide();
        }
    };
    
    function addMouseHandling() {
        $('#calorieGraph').on('mousemove', function(event) {
            var bar = barAt(event.offsetX, event.offsetY);
            if (bar) {
                showMouseOverForBar(bar, event);
            } else {
                hideMouseOver();
            }
        });
    };

    return {
        graph : function() {
            drawAxes();
            drawData();
            addMouseHandling();
        }
    };
}();

$(document).ready(function() {
    CalorieGrapher.graph();
});