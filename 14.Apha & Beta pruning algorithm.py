def minimax(depth, player, alpha, beta)
  if gameover or depth == 0
    return calculated_score
  end
  children = all legal moves for player
  if player is AI (maximizing player)
    for each child
      score = minimax(depth - 1, opponent, alpha, beta)
      if (score > alpha)
        alpha = score
      end
      if alpha >= beta
        break
      end
      return alpha
    end
  else #player is minimizing player
    best_score = +infinity
    for each child
      score = minimax(depth - 1, player, alpha, beta)
      if (score < beta)
        beta = score
      end
      if alpha >= beta
        break
      end
      return beta
    end
  end
end

#then you would call it like
minimax(2, computer, -inf, +inf)
