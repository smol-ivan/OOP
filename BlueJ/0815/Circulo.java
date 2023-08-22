public class Circulo{
    
    float radio;
    
    public Circulo(float r) {
        radio = r;
    }
    
    public double getArea () {
        return (Math.PI * radio * radio);
    }
    
    public double getPerimetro () {
        return (2 * Math.PI * radio);
    }
    
}
