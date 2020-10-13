import { Injectable } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  BaseUrl = 'http://localhost:60330/api'
  constructor(private http: HttpClient) { }

  signUp(formModel) {
    var body = {
      UserName: formModel.value.UserName,
      Email: formModel.value.Email,
      Password: formModel.value.Passwords.Password,
    }

    return this.http.post(this.BaseUrl + '/ApplicationUser/Register/', body)
  }

  login(formData) {
    return this.http.post(this.BaseUrl + '/ApplicationUser/Login/', formData)
  }

  getUserProfile() {
    //var tokenHeader = new HttpHeaders({'Authorization': 'Bearer ' + localStorage.getItem('token')})
    return this.http.get(this.BaseUrl + '/UserProfile')
  }




}
