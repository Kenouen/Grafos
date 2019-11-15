package br.edu.ifpb.Grafos;
import java.util.*;

public abstract class Grafo
{
    public Set<Vertice> Vertices;
    public Set<Aresta> Arestas;


    public Grafo() {
        Vertices = new HashSet<>();
        Arestas = new HashSet<>();
    }

    public boolean verticeValido(String vertice){
        return !vertice.equals("") && !vertice.equals(" ") && vertice.length() != 1;
    }

    public boolean arestaValido(String aresta){
        String novo1 = String.format("%c", aresta.charAt(0));
        String novo2 = String.format("%c", aresta.charAt(aresta.length()-1));

        return !verticeValido(novo1) &&
                !verticeValido(novo2);
    }

    @Override
    public String toString() {

        System.out.println(Vertices.toString());
        System.out.println(Arestas.toString());

        return null;
    }
}
