import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PerfiluseradminComponent } from './perfiluseradmin.component';

describe('PerfiluseradminComponent', () => {
  let component: PerfiluseradminComponent;
  let fixture: ComponentFixture<PerfiluseradminComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PerfiluseradminComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PerfiluseradminComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
