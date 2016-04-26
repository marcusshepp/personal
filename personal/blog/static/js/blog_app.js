var blog_app = angular.module("blog_app", []);

blog_app.config(["$interpolateProvider", function($interpolateProvider){
    $interpolateProvider.startSymbol("{[");
    $interpolateProvider.endSymbol("]}");
}]);

blog_app.controller("category_controller", ["$scope", "$http",
    function($scope, $http){
        $http({
            method: "GET",
            url: "/blog/api/categories",
        }).then(function successCallback(response){
            console.log(response);
        }, function errorCallback(response){
            console.log(response);
        });
    }]);
