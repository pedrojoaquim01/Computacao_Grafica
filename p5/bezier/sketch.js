let pontos = [];
let selecionado = null;

let p1, p2, p3;

function setup() {
    createCanvas(600,600);
    
    pontos.push(createVector(10,height/2));
    pontos.push(createVector(width-10,height/2));
    pontos.push(createVector(width/2 - 50,height/2 - 50));
    pontos.push(createVector(width/2 + 50,height/2 - 50));
}  

function segmento(A,B) {
    line(A.x, A.y, B.x, B.y);
}

function ponto(A) {
    circle(A.x,A.y,10);
}

function combina(A,B,t) {
    return {x:(1-t)*A.x+t*B.x,y:(1-t)*A.y+t*B.y};
}

function draw() {
    background(200);

    p1 = {x:pontos[0].x,y:pontos[0].y};
    p2 = {x:pontos[1].x,y:pontos[1].y};
    p3 = {x:pontos[2].x,y:pontos[2].y};
    p4 = {x:pontos[3].x,y:pontos[3].y};

    noFill();
    beginShape();
    for(let t=0; t<=1; t+=0.01)
    {
        A = combina(p1,p3,t);
        B = combina(p3,p4,t);
        C = combina(p4,p2,t);
        
        E = combina(A,B,t);
        F = combina(B,C,t);

        G = combina(E,F,t);
        vertex(G.x,G.y);
    }
    endShape();

    let vmouse = createVector(mouseX,mouseY);
    selecionado = null;
    for(let p of pontos) {
        if(vmouse.dist(p)<10) {
            selecionado = p;
            fill("#ff0000");
        } else {
            fill("#ffffff");
        }
        ponto(p);
    }

}

function mouseDragged()
{
    if(selecionado) {
        selecionado.set(mouseX, mouseY);
    }
}