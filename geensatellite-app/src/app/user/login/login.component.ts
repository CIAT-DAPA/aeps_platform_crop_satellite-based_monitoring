import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, NgForm } from '@angular/forms';
import { UserService } from 'src/app/shared/user.service';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  formModel
  constructor(private fb: FormBuilder, private api: UserService, private router: Router, private toastr: ToastrService) {

    this.formModel = ({
      UserName: '',
      Password: ''
    })
  }

  ngOnInit(): void {
    if (localStorage.getItem('token') != null)
    this.router.navigateByUrl('/home');
  }

  onSubmit(form: NgForm) {
    this.api.login(form.value).subscribe(
      (res: any) => {
        localStorage.setItem('token', res.token);
        this.router.navigateByUrl('/home/index')
      }, (error) => {
        if (error == 400)
          this.toastr.error('Incorrect username or password.', 'Authentication failed');
        else
          console.log(error);


      }
    )
  }

}
