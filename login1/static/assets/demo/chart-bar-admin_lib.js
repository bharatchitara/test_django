// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

//console.log(moment().subtract(6, 'months').format('MMM'))

// Bar Chart Example
var month_lib = document.getElementById("mon_list").value;
console.log(month_lib)


var year = document.getElementById("year_list").value;
console.log(year)

var book_count_lib = document.getElementById("lib_list").value;
console.log(book_count_lib)

var up_month_lib = [];
var up_book_count_lib = [];
var up_year = [];
var final_up_month = [];

month_lib  = month_lib.replace('[','')
month_lib  = month_lib.replace(']','')
year  = year.replace('[','')
year  = year.replace(']','')


for(var i = 0 ; i< book_count_lib.length;i++){
    book_count_lib = book_count_lib.replace('[','')
    book_count_lib = book_count_lib.replace(']','')
}
console.log("book_count"+book_count_lib)


const split_string_lib = month_lib.split(" ");
const split_string1_lib = year.split(" ");
const split_string_of_book_count_lib = book_count_lib.split(" ");

console.log(split_string_of_book_count_lib)

for(var i =0 ;i< split_string_lib.length;i++){

split_string_lib[i] = split_string_lib[i].replace(',','')
split_string_lib[i] = split_string_lib[i].replace(/["']/g, "")

split_string1_lib[i] = split_string1_lib[i].replace(',','')
split_string1_lib[i] = split_string1_lib[i].replace(/["']/g, "")

split_string_of_book_count_lib[i] = split_string_of_book_count_lib[i].replace(',','')
split_string_of_book_count_lib[i] = split_string_of_book_count_lib[i].replace(/["']/g, "")




up_month_lib.push(split_string_lib[i])
up_book_count_lib.push(split_string_of_book_count_lib[i])
up_year.push(split_string1_lib[i])

}
//console.log("data")
console.log(up_book_count_lib)


for (var i = 0 ;i<up_month_lib.length;i++){
  value = ( up_month_lib[i] +" "+ up_year[i])
  final_up_month.push(value)
}

console.log(final_up_month)


var max_num = Math.max(...up_book_count_lib)
console.log(max_num)

var current_scale = 10

if (max_num > current_scale){
  //current_scale = max_num + 20
  mod = max_num % 10

  current_scale = max_num + 10 - mod 

}





var ctx = document.getElementById("myBarChart2");
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    //for(let i =0 ; i< up_month.length;i++){
    labels: [final_up_month[5],final_up_month[4],final_up_month[3],final_up_month[2],final_up_month[1],final_up_month[0]],  //x-axis
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
          max: current_scale,
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
