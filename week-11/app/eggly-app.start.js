angular.module('Eggly', [

])
.controller('MainCtrl', function($scope) {
  $scope.categories = [
    {"id": 0, "name": "Development"},
    {"id": 1, "name": "Development1"},
    {"id": 2, "name": "Development2"},
    {"id": 3, "name": "Humor"}
  ];

  $scope.bookmarks = [
    {"id": 0, "title": "AngularJS 0", "url": "http://angularjs.org", "category": "Development"},
    {"id": 1, "title": "AngularJS 1", "url": "http://angularjs.org", "category": "Development"},
    {"id": 2, "title": "AngularJS 2", "url": "http://angularjs.org", "category": "Development"},
    {"id": 3, "title": "Humor 3", "url": "http://angularjs.org", "category": "Humor"},
    {"id": 4, "title": "Humor 4", "url": "http://angularjs.org", "category": "Humor"}
  ];

  $scope.currentCategory = null;

  function setCurrentCategory(category) {
    $scope.currentCategory = category;
  }

  function isCurrentCategory(category) {
    return $scope.currentCategory !== null && category.name === $scope.currentCategory.name;
  }

  $scope.setCurrentCategory = setCurrentCategory;
  $scope.isCurrentCategory = isCurrentCategory;
})
;
