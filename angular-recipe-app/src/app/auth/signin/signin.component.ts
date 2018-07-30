import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent implements OnInit {

  hasError = false

  constructor(private authService: AuthService) { }

  ngOnInit() {
    this.authService.error.subscribe(err => {
      this.hasError = true
    })
  }

  onSignIn(form: NgForm) {
    const username = form.value.username
    const pw = form.value.password
    this.authService.loginUser(username, pw)
  }
}
