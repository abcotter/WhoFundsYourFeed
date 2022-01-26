export const PieChartData = {
    type: "doughnut",
    data: {
      labels: ["Mercury", "Venus", "Earth"],
      datasets: [
        {
          label: "Number of Moons",
          data: [82, 27, 14],
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