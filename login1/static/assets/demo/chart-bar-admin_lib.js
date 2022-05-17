// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

//console.log(moment().subtract(6, 'months').format('MMM'))

// Bar Chart Example
var month_lib = document.getElementById("mon_list").value;
console.log(month_lib)

var book_count_lib = document.getElementById("lib_list").value;
console.log(book_count_lib)

var up_month_lib = [];
var up_book_count_lib = [];

month_lib  = month_lib.replace('[','')
month_lib  = month_lib.replace(']','')

for(var i = 0 ; i< book_count_lib.length;i++){
    book_count_lib = book_count_lib.replace('[','')
    book_count_lib = book_count_lib.replace(']','')
}
console.log("book_count"+book_count_lib)


const split_string_lib = month_lib.split(" ");
const split_string_of_book_count_lib = book_count_lib.split(" ");

console.log(split_string_of_book_count_lib)

for(var i =0 ;i< split_string_lib.length;i++){

split_string_lib[i] = split_string_lib[i].replace(',','')
split_string_lib[i] = split_string_lib[i].replace(/["']/g, "")

split_string_of_book_count_lib[i] = split_string_of_book_count_lib[i].replace(',','')
split_string_of_book_count_lib[i] = split_string_of_book_count_lib[i].replace(/["']/g, "")




up_month_lib.push(split_string_lib[i])
up_book_count_lib.push(split_string_of_book_count_lib[i])

}
//console.log("data")
console.log(up_book_count_lib)

var ctx = document.getElementById("myBarChart2");
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    //for(let i =0 ; i< up_month.length;i++){
    labels: [up_month_lib[5],up_month_lib[4],up_month_lib[3],up_month_lib[2],up_month_lib[1],up_month_lib[0]],  //x-axis
    //}
    datasets: [{
      label: "Librarians",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [up_book_count_lib[5],up_book_count_lib[4],up_book_count_lib[3],up_book_count_lib[2],up_book_count_lib[1],up_book_count_lib[0]],      //y-axis
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 6
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 10,
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
