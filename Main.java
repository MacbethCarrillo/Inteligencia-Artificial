package IA;

public class Main {
    public static void main(String[] args) {
        Arbol arbol = new Arbol();
        arbol.insertar(5);
        arbol.insertar(3);
        arbol.insertar(7);
        arbol.insertar(2);
        arbol.insertar(4);
        arbol.insertar(6);
        arbol.insertar(8);

        System.out.println("Árbol:");
        arbol.imprimirArbol();

        int valorBuscado = 6;
        Nodo nodoEncontrado = arbol.buscarNodo(valorBuscado);
        if (nodoEncontrado != null) {
            System.out.println("El nodo con valor " + valorBuscado + " fue encontrado.");
        } else {
            System.out.println("El nodo con valor " + valorBuscado + " no fue encontrado.");
        }
    }
}
