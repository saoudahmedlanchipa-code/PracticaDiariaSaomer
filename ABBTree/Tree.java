
package ABBTree;
    
public interface Tree<E> extends Iterable<E> {
    /** Retorna true si el elemento esta en el árbol */
    public boolean search(E e);

    /** Inserta elemento en un ábol binario de búsqueda.
     * Retorna verdadero si el elemento es insertado exitosamente. */
    public boolean insert(E e);

    /** Borra el element especificado desde el árbol.
     * Retorna verdadero si el elemento es borrado exitosamente. */
    public boolean delete(E e);

    /** Recorre el árbol en inorden*/
    public void inorder();
     
    /** Postorden recorrido desde la raiz */
    public void postorder();

       /** Preorden recorrido es desde la raiz */
       public void preorder();

       /** Obtiene el número de nodos en el árbol */
       public int getSize();

       /** Retorna true si el árbol esta vacío */
       public boolean isEmpty();

       /** Deja el arbol vacio */
       public void clear();
}


