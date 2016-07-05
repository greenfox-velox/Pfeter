'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

const student = {
  grades: [],
  addGrade: function (grade) {
    this.grades.push(grade);
  },
  getAverage: function () {
    let summ = 0;
    this.grades.forEach(function (e) {
      summ += e;
    });
    return summ / this.grades.length;
  },
};

student.addGrade(5);
student.addGrade(1);
console.log(student.getAverage());
