import { Injectable } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser'
import { HttpHeaders, HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class FilterService {
  ENDPOINT = 'http://localhost:8000'
  headers = new HttpHeaders({
    'Content-Type': 'application/json',
  })
  headersGraphic = new HttpHeaders({
    'Content-Type': 'image/svg+xml',
  })
  constructor(private http: HttpClient, private sanitizer: DomSanitizer) { }

  //Method get data about dataframe
  getDataframe(startDate, endDate, area, lon, lat): Observable<any> {
    //use httClient for set api data about sentinel2
    return this.http.get(this.ENDPOINT + `/paintmap/${startDate}/${endDate}/${area}/${lon}/${lat}`, { headers: this.headers })
  }

  //Method get data about associations
  getAssociation(): Observable<any> {
    //use httClient for set api data about associations
    return this.http.get(this.ENDPOINT + '/api/associations/', { headers: this.headers })
  }

  //Method get data about associations
  getTechnicalAssistants(association): Observable<any> {
    //use httClient for set api data about associations
    return this.http.get(this.ENDPOINT + '/api/technical-assistant/' + association + '/get/', { headers: this.headers })
  }

  //Method get data about associations
  getProductionEvents(technical, plot): Observable<any> {
    //use httClient for set api data about associations
    return this.http.get(this.ENDPOINT + '/api/production-events/' + technical + '/' + plot + '/get/', { headers: this.headers })
  }

  //Method get data about associations
  getFarmerByTechnical(technical): Observable<any> {
    //use httClient for set api data about associations
    return this.http.get(this.ENDPOINT + '/api/production-event/' + technical + '/get/', { headers: this.headers })
  }

  //Method get data about associations
  getPlots(farm): Observable<any> {
    //use httClient for set api data about associations
    return this.http.get(this.ENDPOINT + '/api/plots/' + farm + '/get/', { headers: this.headers })
  }

  //Method get data about associations
  getFarm(): Observable<any> {
    //use httClient for set api data about associations
    return this.http.get(this.ENDPOINT + '/api/farm/', { headers: this.headers })
  }

  //Method get data about associations
  getBlockForm(form): Observable<any> {
    //use httClient for set api data about associations
    return this.http.get(this.ENDPOINT + '/api/block-form/' + form + '/get/', { headers: this.headers })
  }

  //Method get data about associations
  getQuestion(form, type): Observable<any> {
    //use httClient for set api data about associations
    return this.http.get(this.ENDPOINT + '/api/question/' + form + '/' + type + '/get/', { headers: this.headers })
  }

  //Method get data about associations
  getResponsesNumeric(question, event): Observable<any> {
    //use httClient for set api data about associations
    return this.http.get(this.ENDPOINT + '/api/question-numeric/' + question + '/' + event + '/get/', { headers: this.headers })
  }

  //Method get data about associations
  getResponsesDate(question, event): Observable<any> {
    //use httClient for set api data about associations
    return this.http.get(this.ENDPOINT + '/api/question-date/' + question + '/' + event + '/get/', { headers: this.headers })
  }

  getMap(index, startDate, endDate, area, lon, lat): Observable<any> {
    /* Method get data about associations */
    //use httClient for set api data about associations
    return this.http.get(this.ENDPOINT + `/viewmap/${index}/${startDate}/${endDate}/${area}/${lon}/${lat}`,
      { headers: this.headers, responseType: 'text' }).pipe(map(res => this.sanitizer.bypassSecurityTrustHtml(res)))

    /* { headers: this.headers }).pipe(map(res) this.sanitizer.bypassSecurityTrustHtml(res)) */
  }

  getGraph(startDate, endDate, area, lon, lat): Observable<any> {
    /* Method get data about associations */
    //use httClient for set api data about associations
    return this.http.get(this.ENDPOINT + `/viewchart/${startDate}/${endDate}/${area}/${lon}/${lat}/`,
      { headers: this.headersGraphic, responseType: 'text' }).pipe(map(res => this.sanitizer.bypassSecurityTrustHtml(res)))

    /* { headers: this.headers }).pipe(map(res) this.sanitizer.bypassSecurityTrustHtml(res)) */
  }

  getDataPlot(startDate, endDate, area, lon, lat): Observable<any> {
    /* Method get data about associations */
    //use httClient for set api data about associations
    return this.http.get(this.ENDPOINT + `/bands-table/${startDate}/${endDate}/${area}/${lon}/${lat}`,{ headers: this.headers })

    /* { headers: this.headers }).pipe(map(res) this.sanitizer.bypassSecurityTrustHtml(res)) */
  }


}
