// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Area Chart Example
var month = document.getElementById("mon_list").value;
console.log(month)

var book_count = document.getElementById("book_list").value;
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




var ctx = document.getElementById("myAreaChart1");
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: [up_month[5],up_month[4],up_month[3],up_month[2],up_month[1],up_month[0]],
    datasets: [{
      label: "Books",
      lineTension: 0.3,
      backgroundColor: "rgba(2,117,216,0.2)",
      borderColor: "rgba(2,117,216,1)",
      pointRadius: 5,
      pointBackgroundColor: "rgba(2,117,216,1)",
      pointBorderColor: "rgba(255,255,255,0.8)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(2,117,216,1)",
      pointHitRadius: 50,
      pointBorderWidth: 2,
      data: [up_book_count[5],up_book_count[4],up_book_count[3],up_book_count[2],up_book_count[1],up_book_count[0]],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'Month'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 60,
          maxTicksLimit: 5
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
