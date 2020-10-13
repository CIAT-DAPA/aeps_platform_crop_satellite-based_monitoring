import { BrowserModule } from '@angular/platform-browser';
import { LOCALE_ID, NgModule } from '@angular/core';
import { DatePipe } from '@angular/common';

import { AppRoutingModule } from './app-routing.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms'
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http'
import { AppComponent } from './app.component';
import { FilterComponent } from './filter/filter.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { SafePipeModule } from 'safe-pipe';
//material
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSelectModule } from '@angular/material/select';
import { NgxMatSelectSearchModule } from 'ngx-mat-select-search';
import { NgxPaginationModule } from 'ngx-pagination';
import { NgxSpinnerModule } from "ngx-spinner";
import {MatSidenavModule} from '@angular/material/sidenav';
import { MatListModule } from "@angular/material/list";
import { MatIconModule } from "@angular/material/icon";
import { MatToolbarModule } from "@angular/material/toolbar";
import { MatMenuModule } from "@angular/material/menu";
import { MatCardModule } from "@angular/material/card";

import { registerLocaleData } from '@angular/common';
import localeEsCO from '@angular/common/locales/es-CO';
import { ToastrModule } from 'ngx-toastr';

//Local imports
import { LoginComponent } from './user/login/login.component';
import { UserComponent } from './user/user/user.component';
import { SpinnerComponent } from './elements/spinner/spinner.component';
import { RegistrationComponent } from './user/registration/registration.component';
import { HomeComponent } from './home/home.component';
import { UserService } from './shared/user.service';
import { AuthInterceptor } from './auth/auth.interceptor';
import { MainNavComponent } from './main-nav/main-nav.component';
import { LayoutModule } from '@angular/cdk/layout';
import { MatButtonModule } from '@angular/material/button';
import { SafePipe } from './safe.pipe';
import { PlotComponent } from './elements/plot/plot.component';

registerLocaleData(localeEsCO, 'es-Co');

@NgModule({
  declarations: [
    AppComponent,
    FilterComponent,
    LoginComponent,
    UserComponent,
    SpinnerComponent,
    RegistrationComponent,
    HomeComponent,
    MainNavComponent,
    SafePipe,
    PlotComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    MatSidenavModule,
    MatListModule,
    MatIconModule,
    MatToolbarModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    MatFormFieldModule,
    NgxMatSelectSearchModule,
    MatSelectModule,
    NgxPaginationModule,
    NgxSpinnerModule,
    ToastrModule.forRoot({
      progressBar: true
    }
    ),
    LayoutModule,
    MatButtonModule,
    MatMenuModule,
    MatCardModule,
    SafePipeModule
  ],
  providers: [UserService, {
    provide: HTTP_INTERCEPTORS,
    useClass: AuthInterceptor,
    multi: true
  }, { provide: LOCALE_ID, useValue: 'es-Co' }, DatePipe],
  bootstrap: [AppComponent]
})
export class AppModule { }
