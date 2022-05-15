// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

//console.log(moment().subtract(6, 'months').format('MMM'))

// Bar Chart Example
var month = document.getElementById("mon_list").value;

var book_count = document.getElementById("book_count_list").value;
console.log(book_count)

var up_month = [];
var up_book_count = [];

month  = month.replace('[','')
month  = month.replace(']','')

for(var i = 0 ; i< book_count.length;i++){
    book_count = book_count.replace('[','')
    book_count = book_count.replace(']','')
}
console.log(book_count)


const split_string = month.split(" ");
const split_string_of_book_count = book_count.split(" ");

console.log(split_string_of_book_count)

for(var i =0 ;i< split_string.length;i++){

split_string[i] = split_string[i].replace(',','')
split_string[i] = split_string[i].replace(/["']/g, "")

split_string_of_book_count[i] = split_string_of_book_count[i].replace(',','')
split_string_of_book_count[i] = split_string_of_book_count[i].replace(/["']/g, "")




up_month.push(split_string[i])
up_book_count.push(split_string_of_book_count[i])

}
//console.log("data")
console.log(up_book_count)

var ctx = document.getElementById("myBarChart");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    //for(let i =0 ; i< up_month.length;i++){
    labels: [up_month[5],up_month[4],up_month[3],up_month[2],up_month[1],up_month[0]],  //x-axis
    //}
    datasets: [{
      label: "Books",
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
