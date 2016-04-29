

/* courseNumber = The course index according to the course list on the feedback page 
	copy paste this in the console in the individual course's feedback page.


*/
$rating = 4;
$courseNumber = 7; 

$scope = angular.element('[ng-controller=feedbackCourses]').scope()
for($i = 0; $i< scope.course[$courseNumber].question.course.length; $i++){
	$scope.course[$courseNumber].question.course[$i].display = true;
	$scope.course[$courseNumber].question.course[$i].value = $rating;
}
for($i = 0; $i< scope.course[$courseNumber].question.faculty.length; $i++){
	$scope.course[$courseNumber].question.faculty[$i].display = true;
	$scope.course[$courseNumber].question.faculty[$i].value = $rating;
}

$scope.$apply();
$scope.submitFeedback();