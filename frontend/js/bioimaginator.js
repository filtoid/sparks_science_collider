/**
 * Created with IntelliJ IDEA.
 * User: Samuel
 * Date: 17/08/14
 * Time: 11:35
 * To change this template use File | Settings | File Templates.
 */

var heightRange = [150, 200];
var widthRange = [5, 20];
var tempRange = [10, 50];

imagination = function(height, width, temperature){

    Caman("#myCanvas", image(), function () {
        this
            .vibrance(vibrance(height))
            .hue(hue(height))
            //.sharpen(sharpen(width))
            .saturation(saturation(width))
            .brightness(brightness(temperature))
            .clip(clip(temperature))
            .render();
    });

}

image = function(height){
    var range = [1, 22];
    //var string = "images/" + Math.floor(map(height, range, heightRange)) + ".jpg";
    var string = "images/7.jpg";

    return string;
}

vibrance = function(val){
    var range = [-100, 100];
    return map(val, range, heightRange);
}

hue = function(val){
    var range = [0, 90];
    return map(val, range, heightRange);
}

sharpen = function(val){
    var range = [0, 100];
    return map(val, range, widthRange);
}

saturation = function(val){
    var range = [0, 100];
    return map(val, range, widthRange);
}

brightness = function(val){
    var range = [-45, 10];
    return map(val, range, tempRange);
}

clip = function(val){
    var range = [0, 90];
    return map(val, range, tempRange);
}

map = function(val,functionRange, variableRange){
    var percent = val /variableRange[1];
    var diff = functionRange[1] - functionRange[0];
    var outRelative = diff * percent;
    return functionRange[0] + outRelative;
}