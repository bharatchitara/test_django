// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

//console.log(moment().subtract(6, 'months').format('MMM'))

// Bar Chart Example
var month = document.getElementById("mon_list").value;
console.log(month)

var year = document.getElementById("year_list").value;
console.log(year)

var book_count = document.getElementById("stu_list").value;
console.log(book_count)

var up_month = [];
var up_book_count = [];
var up_year = [];
var final_up_month = [];

month  = month.replace('[','')
month  = month.replace(']','')
year  = year.replace('[','')
year  = year.replace(']','')



for(var i = 0 ; i< book_count.length;i++){
    book_count = book_count.replace('[','')
    book_count = book_count.replace(']','')
}
console.log(book_count)


const split_string = month.split(" ");
const split_string1 = year.split(" ");

const split_string_of_book_count = book_count.split(" ");

console.log(split_string_of_book_count)

for(var i =0 ;i< split_string.length;i++){

split_string[i] = split_string[i].replace(',','')
split_string[i] = split_string[i].replace(/["']/g, "")

split_string1[i] = split_string1[i].replace(',','')
split_string1[i] = split_string1[i].replace(/["']/g, "")

split_string_of_book_count[i] = split_string_of_book_count[i].replace(',','')
split_string_of_book_count[i] = split_string_of_book_count[i].replace(/["']/g, "")



up_month.push(split_string[i])
up_book_count.push(split_string_of_book_count[i])
up_year.push(split_string1[i])

}
//console.log("data")
console.log(up_book_count)

for (var i = 0 ;i<up_month.length;i++){
  value = ( up_month[i] +" "+ up_year[i])
  final_up_month.push(value)
}

console.log(final_up_month)



var max_num = Math.max(...up_book_count)
console.log(max_num)

var current_scale = 10

if (max_num > current_scale){
  //current_scale = max_num + 20
  mod = max_num % 10

  current_scale = max_num + 10 - mod 

}

var ctx = document.getElementById("myBarChart1");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    //for(let i =0 ; i< up_month.length;i++){
    labels: [final_up_month[5],final_up_month[4],final_up_month[3],final_up_month[2],final_up_month[1],final_up_month[0]],  //x-axis
    //}
    datasets: [{
      label: "Students",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      data: [up_book_count[5],up_book_count[4],up_book_count[3],up_book_count[2],up_book_count[1],up_book_count[0]],      //y-axis
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
