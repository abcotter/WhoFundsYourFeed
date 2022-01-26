export const PieChartData = {
    type: "doughnut",
    data: {
      labels: ["Sponsored Videos", "Unsponsored Videos"],
      datasets: [
        {
          label: "Watching Stats",
          data: [outputVideoSponsored, 100 - outputVideoSponsored]
          backgroundColor: "rgb(255, 107, 107)",
          borderColor: "#36495d",
          borderWidth: 1,
        }
      ]
    },
    options: {
      responsive: false,
      //lineTension: 1,
      //scales: {
        //yAxes: [
          //{
            //ticks: {
              //beginAtZero: true,
              //padding: 1
            //}
          //}
        //]
      //}
    }
  };
  
  export default PieChartData;