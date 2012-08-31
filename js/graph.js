var CalorieGrapher = function() {
    function drawAxes() {
        var canvas = document.getElementById('calorieGraph');
        if (canvas.getContext) {
            var context = canvas.getContext('2d');
            context.strokeColor = '#000000';
            context.moveTo(10, 10);
            context.lineTo(10, 390);
            context.lineTo(790, 390);
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
    
    function drawBarPart(context, left, top, right, bottom) {
        var color = barColors[lastColor];
        lastColor = (lastColor + 1) % barColors.length;
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
    
    function drawBar(dayData, maxBarPercent, barPosition) {
        var barLeft = barPosition * 30 + 20;
        var barHeight = maxBarPercent * 380;
        var canvas = document.getElementById('calorieGraph');
        var bar = {
            left: barLeft,
            top: 390-barHeight,
            right: barLeft+20,
            bottom: 390,
            day: dayData
        };
        bars.push(bar);
        if (canvas.getContext) {
            var context = canvas.getContext('2d');
            var bottom = bar.bottom;
            var top = bar.bottom;
            var height = 0;
            for (var i=0; i<bar.day.entries.length; i++) {
                height = bar.day.entries[i].calories/bar.day.total_calories*barHeight;
                top -= height;
                drawBarPart(context, bar.left, top, bar.right, bottom);
                bottom -= height;
            }
        } else {
            console.log('No canvas support');
        }    
    };
    
    function drawFetchedData(data) {
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
            drawBar(day, calories/topCalories, i);
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
            $('#pageContent').append('<div id="graphMouseOver"></div>');
            mouseOver = $('#graphMouseOver');
        }
        mouseOver.text(bar.day.date + ': ' + bar.day.total_calories);
        mouseOver.css('left', event.pageX);
        mouseOver.css('top', event.pageY);
        mouseOver.show();
    };
    
    function hideMouseOver() {
        if (mouseOver) {
            mouseOver.hide();
        }
    };
    
    function addMouseOver() {
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
            addMouseOver();
        }
    };
}();

$(document).ready(function() {
    CalorieGrapher.graph();
});