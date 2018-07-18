import { HttpInterceptor, HttpRequest, HttpEvent, HttpHandler } from "@angular/common/http";
import { Observable } from "rxjs";
import { tap } from 'rxjs/operators'

/* Handler that works on the RESPONSE. Logs message on each request */
export class LoggingInterceptor implements HttpInterceptor {

    intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        return next.handle(request).pipe(
            tap(res => console.log("Logging interceptor", res))
        )
    }
}