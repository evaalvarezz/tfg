import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AnadiradminComponent } from './anadiradmin.component';

describe('AnadiradminComponent', () => {
  let component: AnadiradminComponent;
  let fixture: ComponentFixture<AnadiradminComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AnadiradminComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AnadiradminComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
