var CalorieGrapher = function() {
    var AXES_HEIGHT = 390;
    var AXES_WIDTH = 790;
    var AXES_OFFSET = 10;
    var MAX_BAR_HEIGHT = 380;
    var BAR_WIDTH = 35;
    var BAR_SPACE = 15;
    
    var BAR_MODE_ABSOLUTE = 'absolute';
    var BAR_MODE_PERCENTAGE = 'percentage';
    
    var settings = {
        barMode: BAR_MODE_PERCENTAGE
    };
    
    function clear() {
        var canvas = document.getElementById('calorieGraph');
        if (canvas.getContext) {
            var context = canvas.getContext('2d');
            context.clearRect(0, 0, 800, 400);
        } else {
            console.log('No canvas support');
        }
    };

    function drawAxes() {
        var canvas = document.getElementById('calorieGraph');
        if (canvas.getContext) {
            var context = canvas.getContext('2d');
            context.strokeColor = '#000000';
            context.beginPath();
            context.moveTo(AXES_OFFSET, AXES_OFFSET);
            context.lineTo(AXES_OFFSET, AXES_HEIGHT);
            context.lineTo(AXES_WIDTH, AXES_HEIGHT);
            context.stroke();
        } else {
            console.log('No canvas support');
        }    
    };
    
    var BAR_COLORS = [
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
            color = BAR_COLORS[lastColor];
            lastColor = (lastColor + 1) % BAR_COLORS.length;
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
    
    function drawBar(dayData, maxBarPercent, barPosition, displayMode, mode) {
        mode = typeof mode !== 'undefined' ? mode : 'entries';
        var barLeft = barPosition * (BAR_WIDTH + BAR_SPACE) + BAR_SPACE + AXES_OFFSET;
        var barHeight = maxBarPercent * MAX_BAR_HEIGHT;
        if (settings.barMode === BAR_MODE_PERCENTAGE) {
            barHeight = MAX_BAR_HEIGHT;
        }
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
    
    function drawData() {
        for (var i=graphData.startIndex; i<graphData.food_days.length; i++) {
            var day = graphData.food_days[i];
            var calories = day.total_calories;
            drawBar(day, calories/graphData.topCalories, i-graphData.startIndex, BAR_MODE_ABSOLUTE, 'tags');
        }
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
    
    var graphData;
    
    function saveData(data) {
        graphData = data;
        
        for (var i=0; i<graphData.tags.length; i++) {
            tags.push(graphData.tags[i]);
            tag_colors[graphData.tags[i].id] = BAR_COLORS[i%BAR_COLORS.length];
        }
        tags.push({name: 'None', id:0})
        tag_colors[0] = BAR_COLORS[graphData.tags.length%BAR_COLORS.length]
    
        graphData.topCalories = 0;
        graphData.startIndex = 0;
        if (graphData.food_days.length > 14) {
            graphData.startIndex = graphData.food_days.length-14;
        }
        for (var i=graphData.startIndex; i<graphData.food_days.length; i++) {
            var day = graphData.food_days[i];
            var calories = day.total_calories;
            if (graphData.topCalories < calories) {
                graphData.topCalories = calories;
            }
        }
    };
    
    function redrawAll() {
        clear();
        drawAxes();
        drawData();
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
    
    function initialize(data) {
        saveData(data);
        redrawAll();
        addMouseHandling();
    };
    
    function fetchData(callback) {
        $.ajax({
            url: '/graph/data',
            dataType: 'json',
            success: callback
        });
    };

    return {
        initialLoad: function() {
            fetchData(initialize);
        },
        redraw: function() {
            redrawAll();
        },
        
        barModeOptions: function() {
            return [
                BAR_MODE_ABSOLUTE,
                BAR_MODE_PERCENTAGE
            ];
        },
        getBarMode: function() {
            return settings.barMode;
        },
        setBarMode: function(mode) {
            settings.barMode = mode;
        }
    };
}();

$(document).ready(function() {
    CalorieGrapher.initialLoad();
    
    var barModeSelector = $('select[name="barMode"]');
    for (var i=0; i<CalorieGrapher.barModeOptions().length; i++) {
        var mode = CalorieGrapher.barModeOptions()[i];
        var option = $('<option value="' + mode + '">' + mode + '</option>')[0];
        if (mode === CalorieGrapher.getBarMode()) {
            option = $('<option value="' + mode + '" selected="selected">' + mode + '</option>')[0];
        }
        barModeSelector[0].options.add(option);
    }
    barModeSelector.on('change', function() {
        var choice = this.options[this.selectedIndex].value;
        CalorieGrapher.setBarMode(choice);
        CalorieGrapher.redraw();
    });
});