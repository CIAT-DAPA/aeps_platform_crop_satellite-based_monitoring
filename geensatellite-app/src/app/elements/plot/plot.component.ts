import { Component, OnInit, ViewChild, ElementRef, Input } from '@angular/core';
import { FilterService } from 'src/app/services/filter.service';
declare var Plotly: any;

@Component({
  selector: 'app-plot',
  templateUrl: './plot.component.html',
  styleUrls: ['./plot.component.css']
})
export class PlotComponent implements OnInit {
  @Input() drawGraph
  @Input() startDate
  @Input() endDate
  @Input() area
  @Input() lon
  @Input() lat
  @ViewChild("Plot", { static: true })
  private Plot: ElementRef;
  plotData$
  receivedData
  data
  responseDate = []
  responseNdvi = []
  constructor(private api: FilterService) {
    this.plotData$ = {
      date: '',
      ndvi: ''
    }
  }

  getDataPlot() {
    if (this.drawGraph == true) {

      this.api.getDataPlot(this.startDate, this.endDate, this.area, this.lon, this.lat).subscribe(
        (res) => {
        this.plotData$ = res
        res.forEach((dt: any) => {
          this.responseDate.push(
            dt.date
          );
        });
        res.forEach((dt: any) => {
          this.responseNdvi.push(
            dt.ndvi
            );
        });
        this.basicChart()
      }, (err) => {
        console.log(err);
      }
      )
    }
  }

  basicChart() {
    let one = this.responseDate
    let two = this.responseNdvi

    console.log(this.responseDate);
    const element = this.Plot.nativeElement
    const data = [{
      x: one,
      y: two,
      name: 'type string, name of the trace',
      type: 'scatter', //this very important to activate WebGL
      mode: 'lines+markers', //other properties can be found in the docs.,
    }]

    const style = {
      layout: {width: 320, height: 240, title: 'Filter'}
    }
    Plotly.plot(element, data, style)
  }


  plotGraph() {
    this.Plot = Plotly.newPlot(
      this.Plot.nativeElement,
      this.data,
      {
        autoexpand: "true",
        autosize: "true",
        width: window.innerWidth - 200,
        margin: {
          autoexpand: "true",
          margin: 0
        },
        offset: 0,
        type: "scatter",
        title: name, //Title of the graph
        hovermode: "closest",
        xaxis: {
          linecolor: "black",
          linewidth: 2,
          mirror: true,
          title: "Time (s)",
          automargin: true
        },
        yaxis: {
          linecolor: "black",
          linewidth: 2,
          mirror: true,
          automargin: true,
          title: 'Any other Unit'
        }
      },
      {
        responsive: true,
        scrollZoom: true
      });
  }

  ngOnInit(): void {
    this.getDataPlot()
  }

}
