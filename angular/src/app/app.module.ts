import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NabarComponent } from './nabar/nabar.component';
import { PieComponent } from './pie/pie.component';
import { RegistroComponent } from './registro/registro.component';
import { LoginComponent } from './login/login.component';
import { RecetasComponent } from './recetas/recetas.component';
import { ListarecetaComponent } from './listareceta/listareceta.component';
import { PerfiluseradminComponent } from './perfiluseradmin/perfiluseradmin.component';
import { AnadiradminComponent } from './anadiradmin/anadiradmin.component';
import { EditaradminComponent } from './editaradmin/editaradmin.component';

@NgModule({
  declarations: [
    AppComponent,
    NabarComponent,
    PieComponent,
    RegistroComponent,
    LoginComponent,
    RecetasComponent,
    ListarecetaComponent,
    PerfiluseradminComponent,
    AnadiradminComponent,
    EditaradminComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
