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
                console.log(response.data);
                var categories = new Array();
                for (var i = 0; i < response.data.length; i++){
                    categories.push(response.data[i].name);
                }
                $scope.categories = categories;
            }, function errorCallback(response){
                console.log(response);
            });
}]);

blog_app.controller("post_controller", ["$scope", "$http",
    function($scope, $http){
        $http({
            method: "GET",
            url: "/blog/api/posts",
            }).then(function successCallback(response){
                console.log(response.data);
                var posts = new Array();
                for (var i = 0; i < response.data.length; i++){
                    posts.push(
                            [
                                response.data[i].title, 
                                response.data[i].get_body_preview,
                                response.data[i].get_category_name,
                                response.data[i].display_date_created,
                            ]
                    );
                }
                $scope.posts = posts;
            }, function errorCallback(response){
                console.log(response);
            });
}]);
