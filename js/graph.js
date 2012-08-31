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
            log.console('No canvas support');
        }    
    };
    
    function drawBar(maxBarPercent, barPosition) {
        var barLeft = barPosition * 30 + 20;
        var barHeight = maxBarPercent * 380;
        console.log("Bar starts at " + barLeft + "," + barHeight);
        var canvas = document.getElementById('calorieGraph');
        if (canvas.getContext) {
            var context = canvas.getContext('2d');
            context.fillColor = '#000000';
            context.strokeColor = '#000000';
            context.beginPath()
            context.moveTo(barLeft, 390-barHeight);
            context.lineTo(barLeft, 390);
            context.lineTo(barLeft + 20, 390);
            context.lineTo(barLeft + 20, 390-barHeight);
            context.closePath();
            context.fill();
        } else {
            log.console('No canvas support');
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
            drawBar(calories/topCalories, i);
        }
    };
    
    function drawData() {
        $.ajax({
            url: '/graph/data',
            dataType: 'json',
            success: drawFetchedData
        });
    };

    return {
        graph : function() {
            drawAxes();
            drawData();
        }
    };
}();

$(document).ready(function() {
    CalorieGrapher.graph();
});