import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators, FormGroup } from '@angular/forms';
import { UserService } from 'src/app/shared/user.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {
  formModel: FormGroup
  constructor(private fb: FormBuilder, private api: UserService, private toastr: ToastrService) {
    this.formModel = this.fb.group({
      UserName: ['', Validators.required],
      Email: ['', Validators.email],
      Passwords: this.fb.group({
        Password: ['', [Validators.required, Validators.minLength(4)]],
        ConfirmPassword: ['', Validators.required]
      }, { validator: this.comparePasswords })
    })
  }

  comparePasswords(fb: FormGroup) {
    let ConfirmPasswordCtrl = fb.get('ConfirmPassword');
    //passwordMismatch
    //confirmPswrdCtrl.error={passwordMismatch:true}
    if (ConfirmPasswordCtrl.errors == null || 'passwordMismatch' in ConfirmPasswordCtrl.errors) {
      if (fb.get('Password').value != ConfirmPasswordCtrl.value)
        ConfirmPasswordCtrl.setErrors({ passwordMismatch: true })
      else
        ConfirmPasswordCtrl.setErrors(null)
    }
  }

  onSubmit() {
    this.api.signUp(this.formModel).subscribe(
      (res: any) => {
        if (res.succeeded) {
          this.formModel.reset()
          this.toastr.success('New user created', 'Registration successful')
        } else {
          res.errors.forEach(element => {
            switch (element.code) {
              case 'DuplicateUserName':
                this.toastr.error('Username is already token', 'Registration failed')
                //Username is already token
                break;
                
                default:
                  this.toastr.error(element.description, 'Registration failed')
                //Registration failed
                break
            }
          });
        }
      },
      (error) => {

      }
    )
  }

  ngOnInit(): void {
    this.formModel.reset()
  }

}
