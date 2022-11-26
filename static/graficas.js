var options = {
    series: [{
      name: tituloy,
      data: lista
  }],
    chart: {
    height: 850,
    type: 'line',
    zoom: {
      enabled: false
    }
  },
  dataLabels: {
    enabled: false
  },
  title: {
    text: titulo,
    align: 'center'
  },
  grid: {
    row: {
      colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
      opacity: 0.5
    },
  },
  yaxis: {
    title: {
        text: tituloy,
        rotate: -90,
        offsetX: 0,
        offsetY: 0,
        style: {
            color: undefined,
            fontSize: '16px',
            fontFamily: 'Helvetica, Arial, sans-serif',
            fontWeight: 600,
            cssClass: 'apexcharts-yaxis-title',
        },
    },
  },
  xaxis: {
    categories: etiquetas,
    title: {
        text: "Tiempo (Hora:Minuto:Segundo)",
        offsetX: 0,
        offsetY: 100,
        style: {
            color: undefined,
            fontSize: '16px',
            fontFamily: 'Helvetica, Arial, sans-serif',
            fontWeight: 600,
        },
    },
  },
};
  
var chart = new ApexCharts(document.querySelector("#chartlineal"), options);
chart.render();

