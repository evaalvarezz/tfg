import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditaradminComponent } from './editaradmin.component';

describe('EditaradminComponent', () => {
  let component: EditaradminComponent;
  let fixture: ComponentFixture<EditaradminComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EditaradminComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EditaradminComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
