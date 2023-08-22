public class Caja{
    private float length;
    private float width; 
    private float height;
    
    public Caja(float l, float w, float h){
        length = l;
        width = w;
        height = h;
    }
    
    public double getSurfaceArea(){
        return 2*(length * width)+ 2*(length*height) + 2*(width*height);
    }
    
    public double getvolume() {
        return length * width * height;
    }
    
    public double getLateralSurfaceArea(){
        return 2*(length * height) + 2*(width * height);
    }
}
