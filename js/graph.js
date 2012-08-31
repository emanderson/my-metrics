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