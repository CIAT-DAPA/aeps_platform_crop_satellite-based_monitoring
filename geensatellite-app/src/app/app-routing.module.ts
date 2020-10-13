import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FilterComponent } from './filter/filter.component';
import { UserComponent } from './user/user/user.component';
import { LoginComponent } from './user/login/login.component';
import { RegistrationComponent } from './user/registration/registration.component';
import { HomeComponent } from './home/home.component';
import { AuthGuard } from './auth/auth.guard';
import { MainNavComponent } from './main-nav/main-nav.component';
import { PlotComponent } from './elements/plot/plot.component';


const routes: Routes = [
  { path: '', redirectTo: '/user/login', pathMatch: 'full' },
  {
    path: 'user', component: UserComponent,

    children: [
      { path: 'registration', component: RegistrationComponent },
      { path: 'login', component: LoginComponent },
    ]
  },
  {
    path: 'home', component: MainNavComponent, canActivate: [AuthGuard], children: [
      { path: 'search/filter', component: FilterComponent },
      { path: 'index', component: HomeComponent },
      { path: 'map', component: PlotComponent },

    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
