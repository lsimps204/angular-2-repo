import { Directive, OnInit, HostBinding, Input, HostListener } from '@angular/core'

@Directive({
    selector: '[appHighlight]'
})
export class HighlightDirective implements OnInit {
    @HostBinding('style.backgroundColor') background: string
    @Input() defaultColor: string = 'transparent'
    @Input() highlightColor: string = 'blue'

    constructor() {}

    ngOnInit() {}

    @HostListener('mouseenter') mouseEnter (eventData: Event) {
        this.background = this.highlightColor
    }

    @HostListener('mouseleave') mouseLeave (eventData: Event) {
        this.background = this.defaultColor
    }
}