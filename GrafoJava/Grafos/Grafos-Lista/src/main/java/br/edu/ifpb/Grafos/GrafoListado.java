package br.edu.ifpb.Grafos;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class GrafoListado extends Grafo {

    public GrafoListado(Set<String> vertices) {
        for (String vertex : vertices) {
            if(verticeValido(vertex)) adicionarVertice(vertex);
        }
        this.Arestas = new HashSet<>();
    }

    public GrafoListado(Set<String> vertices, Set<String> arestas) {
        for (String vertex : vertices) {
            if(verticeValido(vertex)) adicionarVertice(vertex);
        }
        for (String aresta : arestas) {
            if(arestaValido(aresta)) adicionarAresta(aresta);
        }
    }

    public boolean adicionarVertice(String vertice){
        if (!verticeValido(vertice))return false;
        Vertice novo = new Vertice(vertice);
        this.Vertices.add(novo);
        return true;
    }

    public boolean adicionarAresta(String aresta){

        String novo1 = String.format("%c", aresta.charAt(0));
        String novo2 = String.format("%c", aresta.charAt(aresta.length()-1));

        if(!verticeValido(novo1) || !verticeValido(novo2)) return false;

        this.Arestas.add(new ArestaNDirecionada(novo1, novo2));
        return true;
    }
}
