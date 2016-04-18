var app = angular.module("myfirstapp", []);
app.config(["$interpolateProvider", function($interpolateProvider){
    $interpolateProvider.startSymbol("{[");
    $interpolateProvider.endSymbol("]}");
}]);
app.controller("MyController", ["$scope", function($scope){
    this.pops = ["bar", "pop", "lol"];
    this.sizes = [["300", "300"], ["200", "200"], ["400", "200"]];
    $scope.multiply = function(v1, v2){
        var total = v1 * v2;
        if (isNaN(total)){
            return "None";
        } else {
            return v1*v2;
        }
    };
}]);

app.controller("CatGenerator", function(){
    this.get_cat = function(){
        alert("foo");
    };
});