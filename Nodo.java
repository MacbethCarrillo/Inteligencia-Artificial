package IA;

class Nodo {
    int valor;
    Nodo izquierda;
    Nodo derecha;

    Nodo(int valor) {
        this.valor = valor;
        izquierda = null;
        derecha = null;
    }
}

class Arbol {
    Nodo raiz;

    boolean vacio() {
        return raiz == null;
    }

    void insertar(int valor) {
        raiz = insertarRecursivo(raiz, valor);
    }

    private Nodo insertarRecursivo(Nodo nodo, int valor) {
        if (nodo == null) {
            return new Nodo(valor);
        }

        if (valor < nodo.valor) {
            nodo.izquierda = insertarRecursivo(nodo.izquierda, valor);
        } else {
            nodo.derecha = insertarRecursivo(nodo.derecha, valor);
        }

        return nodo;
    }

    void imprimirArbol() {
        imprimirRecursivo(raiz);
    }

    private void imprimirRecursivo(Nodo nodo) {
        if (nodo != null) {
            imprimirRecursivo(nodo.izquierda);
            System.out.println(nodo.valor);
            imprimirRecursivo(nodo.derecha);
        }
    }

    Nodo buscarNodo(int valor) {
        return buscarRecursivo(raiz, valor);
    }

    private Nodo buscarRecursivo(Nodo nodo, int valor) {
        if (nodo == null || nodo.valor == valor) {
            return nodo;
        }

        if (valor < nodo.valor) {
            return buscarRecursivo(nodo.izquierda, valor);
        } else {
            return buscarRecursivo(nodo.derecha, valor);
        }
    }
}
