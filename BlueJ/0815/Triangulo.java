public class Triangulo{
    
    float base, altura;
    
    public Triangulo(float b, float h) {
        base = b;
        altura = h;
    }
    
    public double getPerimetro() {
        return (base + base + base);
    }
    
    public double getArea() {
        return (base * altura / 2);
    }
}
