import { Component, OnInit, ViewChild, ChangeDetectorRef, Pipe } from '@angular/core';
import { DatePipe } from '@angular/common';
import { FilterService } from '../services/filter.service';
import { FormControl } from '@angular/forms';
import { ReplaySubject, Subject } from 'rxjs';
import { take, takeUntil } from 'rxjs/operators';
import { MatSelect } from '@angular/material/select';
import { NgxSpinnerService } from "ngx-spinner";
import { Router } from '@angular/router';


@Component({
  selector: 'app-filter',
  templateUrl: './filter.component.html',
  styleUrls: ['./filter.component.css']
})
export class FilterComponent implements OnInit {

  associations = []
  runGraph = false
  statusDescription = false
  map
  graph
  draw = false
  dataframe = []
  technicalAssistant = []
  technicalAssistantFilter = []
  productionEvents = []
  blockForms = []
  plots = []
  farms = []
  question = []
  questionDate = []
  responsesNumeric = []
  responsesDate = []
  modelFilter
  selectedItems = []
  type = {}
  headers = []
  pageActual = 1
  spinnerSho = false

  /* Variables to filter the dataframe */
  startDate
  endDate
  area
  lon
  lat
  /** control for the selected farm */
  public farmCtrl: FormControl = new FormControl()

  /** control for the MatSelect filter keyword */
  public farmFilterCtrl: FormControl = new FormControl()

  /** list of farm filtered by search keyword */
  public filteredFarm: ReplaySubject<any> = new ReplaySubject<any>(1)

  @ViewChild('singleSelect') singleSelect: MatSelect;

  /** Subject that emits when the component has been destroyed. */
  protected _onDestroy = new Subject<void>();


  constructor(private api: FilterService, private datePipe: DatePipe, private spinner: NgxSpinnerService, private route: Router) {
    this.getAssociation()
    this.modelFilter = {
      association: '',
      technicalAssistant: '',
      farm: '',
      productionEvent: '',
      plot: '',
      blockForm: '',
      blockFormDate: '',
      questionType: '',
      questionTypeDate: '',
      sentinel: '',
      question: '',
      questionDate: ''
    }
    this.type = [
      'string',
      'int',
      'double',
      'date',
      'unique',
      'multiple',
      'geopoint'
    ]
    this.headers = [
      'Index',
      'Date',
      'Cover Percentage',
      'Action'
    ]
    this.responsesNumeric = [
      {
        'id': '',
        'fixed_value': ''
      }
    ]

    this.responsesDate = [
      {
        'id': '',
        'fixed_value': ''
      }
    ]
  }

  getAssociation = () => {
    this.api.getAssociation().subscribe(
      (data) => {
        this.associations = data
        console.log(data);
        //this.getTechnicalAssistants(data.id)

      },
      (error) => {
        console.log(error);
      }
    )
  }
  getTechnicalAssistants = (association) => {
    this.api.getTechnicalAssistants(association).subscribe(
      (data) => {
        this.technicalAssistant = data
        console.log(data);

      },
      (error) => {
        console.log(error);
      }
    )
  }
  getProductionEvents = (technical, plot) => {
    this.api.getProductionEvents(technical, plot).subscribe(
      (data) => {
        this.productionEvents = data
        console.log(data);

      },
      (error) => {
        console.log(error);
      }
    )
  }
  toDateFormat(f) {
    /* Function that format date for dataframe sentinel */
    return this.datePipe.transform(f, "yyyy-MM-dd")
  }

  haToMeter(ha) {
    /* Function that parse Ha to Meter */
    let haValue = 10000
    let equivalentMeter = ha * haValue
    let radius = Math.sqrt(equivalentMeter/Math.PI)
    return radius
  }

  addDays(date, days) {
    /* Add days to date */
    var result = new Date(date);
    result.setDate(result.getDate() + days);
    return result;
  }

  getFarmerByTechnical = (technical) => {
    this.api.getFarmerByTechnical(technical).subscribe(
      (data) => {
        console.log(data);
        this.farms = data
        console.log(this.farms);

      },
      (error) => {
        console.log(error);
      }
    )
  }
  getPlots = (farm) => {
    this.api.getPlots(farm).subscribe(
      (data) => {
        this.plots = data
        console.log(data);

      },
      (error) => {
        //console.log(error);
      }
    )
  }

  getBlockForm = (form) => {
    this.api.getBlockForm(form).subscribe(
      (data) => {
        this.blockForms = data
        console.log(data);
        this.getQuestion(form, 'double')
        this.getQuestionDate(form, 'date')

      },
      (error) => {
        console.log(error);
      }
    )
  }

  getQuestion = (form, type) => {
    this.api.getQuestion(form, type).subscribe(
      (data) => {
        this.question = data
        console.log(data);

      },
      (error) => {
        console.log(error);
      }
    )
  }

  getQuestionDate = (form, type) => {
    this.api.getQuestion(form, type).subscribe(
      (data) => {
        this.questionDate = data
      },
      (error) => {
        console.log(error);
      }
    )
  }

  getResponsesNumeric = (question, event) => {
    this.api.getResponsesNumeric(question, event).subscribe(
      (data) => {
        this.responsesNumeric = data
        console.log(data);
        this.area = this.haToMeter(data[0].fixed_value)

      },
      (error) => {
        console.log(error);
      }
    )
  }
  getResponsesDate = (question, event) => {
    this.api.getResponsesDate(question, event).subscribe(
      (data) => {
        this.responsesDate = data
        this.startDate = this.toDateFormat(data[0].fixed_value)
        this.endDate = this.toDateFormat(this.addDays(data[0].fixed_value, 140))
        this.lon = this.modelFilter.plot.longitude
        this.lat = this.modelFilter.plot.latitude
        this.statusDescription = true
      },
      (error) => {
        console.log(error);
      }
    )
  }

  drawMap(index) {
    this.ShowSpinner()
    this.runGraph = true
    this.map = this.api.getMap(index, this.startDate, this.endDate, this.area, this.lon, this.lat)
  }


  getDataframe = () => {
    this.api.getDataframe(this.startDate, this.endDate, this.area, this.lon, this.lat).subscribe(
      (data) => {
        this.dataframe = data
        this.route.navigate(['home/search/filter'], {fragment: 'overcomes'})

      },
      (error) => {
        console.log(error);
      }
    )
  }

  ShowSpinner() {
    this.spinner.show();

    setTimeout(() => {
      /** spinner ends after 5 seconds */
      this.spinner.hide();
    }, 10000);
  }

  ngOnInit(): void {

    //this.graph = this.api.getGraph(this.startDate, this.endDate, this.area, this.lon, this.lat)
    // set initial selection
    this.farmCtrl.setValue(this.farms[10]);

    // load the initial bank list
    this.filteredFarm.next(this.farms.slice());

    // listen for search field value changes
    this.farmFilterCtrl.valueChanges
      .pipe(takeUntil(this._onDestroy))
      .subscribe(() => {
        this.filterBanks();
      });

  }

  ngAfterViewInit() {
    this.setInitialValue();
  }

  ngOnDestroy() {
    this._onDestroy.next();
    this._onDestroy.complete();
  }

  viewlog(item) {
    console.log(item.id);

  }

  /**
 * Sets the initial value after the filteredBanks are loaded initially
 */
  protected setInitialValue() {
    this.filteredFarm
      .pipe(take(1), takeUntil(this._onDestroy))
      .subscribe(() => {
        // setting the compareWith property to a comparison function
        // triggers initializing the selection according to the initial value of
        // the form control (i.e. _initializeSelection())
        // this needs to be done after the filteredBanks are loaded initially
        // and after the mat-option elements are available
        this.singleSelect.compareWith = (a: any, b: any) => a && b && a.id === b.id;
      });
  }

  cleaned() {
    this.modelFilter = {}
    this.associations = []
    this.runGraph = false
    this.statusDescription = false
    this.map = []
    this.graph = []
    this.dataframe = []
    this.technicalAssistant = []
    this.technicalAssistantFilter = []
    this.productionEvents = []
    this.blockForms = []
    this.plots = []
    this.farms = []
    this.question = []
    this.questionDate = []
    this.responsesNumeric = []
    this.responsesDate = []
    this.selectedItems = []
    this.type = {}
    /* Variables to filter the dataframe */
    this.startDate = ''
    this.endDate = ''
    this.area = ''
    this.lon = ''
    this.lat = ''
    this.getAssociation()
  }

  protected filterBanks() {
    if (!this.farms) {
      return;
    }
    // get the search keyword
    let search = this.farmFilterCtrl.value;
    if (!search) {
      this.filteredFarm.next(this.farms.slice());
      return;
    } else {
      search = search.toLowerCase();
    }
    // filter the banks
    this.filteredFarm.next(
      this.farms.filter(farm => farm.plot.farm.name.toLowerCase().indexOf(search) > -1)
    );
  }

}
