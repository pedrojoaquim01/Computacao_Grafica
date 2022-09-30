let x = 0;
let y = 0;

let v = 10;
let dx = 1;
let dy = 1;

let cx = 150;
let cy = 275;

let PontoJ = 0;
let PontoI = 0;


function setup() {
    createCanvas(1606,950);
}  



function draw() {

    fill(250, 250, 250,250);
    background(0,100);

    let a = circle(x,y,20);
    let b = rect(1450,mouseY,30,200);
    let c = rect(cx,cy,30,200);

    textSize(100);
    text(PontoI + ' : ' + PontoJ, 650, 150);

    if (x > 1606)
    {
        if (dx == 1) { PontoI +=1; v =8;}
        dx = -1;
    }
    else if (x < 0)
    {   
        if (dx == -1) { PontoJ +=1; v =8;}
        dx = 1;
    }
    if (y > 950)
    {
        dy = -1;
    }
    else if (y < 0)
    {
        dy = 1;
    }

    x = x + v * dx;
    y = y + v * dy;

    if (x > 1450 && x < 1480  && y < mouseY + 200 && y > mouseY)
    {
        dx = -1;
        v = v +0.3;
    }
    if (x > cx  && x < cx + 30 && y < cy + 200 && y > cy)
    {
        dx = 1;
        v = v +0.3;
    }

    if (cy + 100 > y)
    {
        cy = cy - 10;
    }
    if (cy + 100 < y)
    {
        cy = cy + 10;
    }


}

