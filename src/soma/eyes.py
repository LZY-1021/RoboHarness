"""
Eyes (Memory-Augmented RAG) Component

Retrieves experience quintuples of multimodal embeddings and failure attributions
to provide contextual awareness.
"""

from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass
import numpy as np


@dataclass
class ExperienceQuintuple:
    """
    Experience quintuple containing multimodal embeddings and failure attributions.
    
    Structure: (state, action, outcome, embedding, failure_attribution)
    """
    state: Dict[str, Any]
    action: Dict[str, Any]
    outcome: Dict[str, Any]
    embedding: np.ndarray
    failure_attribution: Optional[Dict[str, Any]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "state": self.state,
            "action": self.action,
            "outcome": self.outcome,
            "embedding": self.embedding.tolist() if isinstance(self.embedding, np.ndarray) else self.embedding,
            "failure_attribution": self.failure_attribution
        }


class MemoryAugmentedRAG:
    """
    Memory-Augmented Retrieval-Augmented Generation component.
    
    The "Eyes" of SOMA - retrieves relevant experience quintuples based on
    multimodal embeddings and provides contextual awareness.
    """
    
    def __init__(self, embedding_dim: int = 768):
        """
        Initialize the Memory-Augmented RAG system.
        
        Args:
            embedding_dim: Dimension of the embedding vectors
        """
        self.embedding_dim = embedding_dim
        self.memory_bank: List[ExperienceQuintuple] = []
        self.embedding_index: Optional[np.ndarray] = None
    
    def store_experience(self, quintuple: ExperienceQuintuple) -> None:
        """
        Store an experience quintuple in the memory bank.
        
        Args:
            quintuple: Experience quintuple to store
        """
        if quintuple.embedding.shape[0] != self.embedding_dim:
            raise ValueError(f"Embedding dimension mismatch. Expected {self.embedding_dim}, got {quintuple.embedding.shape[0]}")
        
        self.memory_bank.append(quintuple)
        self._update_index()
    
    def _update_index(self) -> None:
        """Update the embedding index for efficient retrieval."""
        if len(self.memory_bank) > 0:
            embeddings = [exp.embedding for exp in self.memory_bank]
            self.embedding_index = np.vstack(embeddings)
    
    def retrieve_experiences(
        self,
        query_embedding: np.ndarray,
        top_k: int = 5,
        filter_failures: bool = False
    ) -> List[Tuple[ExperienceQuintuple, float]]:
        """
        Retrieve relevant experience quintuples based on similarity.
        
        Args:
            query_embedding: Query embedding vector
            top_k: Number of top experiences to retrieve
            filter_failures: If True, only return experiences with failure attributions
        
        Returns:
            List of tuples containing (experience, similarity_score)
        """
        if len(self.memory_bank) == 0:
            return []
        
        if query_embedding.shape[0] != self.embedding_dim:
            raise ValueError(f"Query embedding dimension mismatch. Expected {self.embedding_dim}, got {query_embedding.shape[0]}")
        
        # Compute cosine similarity
        similarities = self._compute_similarity(query_embedding)
        
        # Get top-k indices
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        # Filter and return results
        results = []
        for idx in top_indices:
            exp = self.memory_bank[idx]
            if filter_failures and exp.failure_attribution is None:
                continue
            results.append((exp, float(similarities[idx])))
        
        return results
    
    def _compute_similarity(self, query_embedding: np.ndarray) -> np.ndarray:
        """
        Compute cosine similarity between query and all stored embeddings.
        
        Args:
            query_embedding: Query embedding vector
        
        Returns:
            Array of similarity scores
        """
        # Normalize query
        query_norm = query_embedding / (np.linalg.norm(query_embedding) + 1e-8)
        
        # Normalize index embeddings
        index_norms = np.linalg.norm(self.embedding_index, axis=1, keepdims=True)
        normalized_index = self.embedding_index / (index_norms + 1e-8)
        
        # Compute cosine similarity
        similarities = np.dot(normalized_index, query_norm)
        
        return similarities
    
    def get_failure_contexts(self) -> List[ExperienceQuintuple]:
        """
        Retrieve all experiences with failure attributions.
        
        Returns:
            List of experience quintuples with failure attributions
        """
        return [exp for exp in self.memory_bank if exp.failure_attribution is not None]
    
    def get_contextual_awareness(
        self,
        query_embedding: np.ndarray,
        top_k: int = 5
    ) -> Dict[str, Any]:
        """
        Get contextual awareness information for a query.
        
        Args:
            query_embedding: Query embedding vector
            top_k: Number of top experiences to consider
        
        Returns:
            Dictionary containing contextual information
        """
        experiences = self.retrieve_experiences(query_embedding, top_k=top_k)
        
        context = {
            "retrieved_experiences": len(experiences),
            "experiences": [exp[0].to_dict() for exp in experiences],
            "similarity_scores": [exp[1] for exp in experiences],
            "failure_rate": sum(1 for exp in experiences if exp[0].failure_attribution is not None) / max(len(experiences), 1)
        }
        
        return context
