import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListarecetaComponent } from './listareceta.component';

describe('ListarecetaComponent', () => {
  let component: ListarecetaComponent;
  let fixture: ComponentFixture<ListarecetaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListarecetaComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListarecetaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
