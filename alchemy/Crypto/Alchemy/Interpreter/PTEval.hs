{-# LANGUAGE DataKinds             #-}
{-# LANGUAGE DeriveFunctor         #-}
{-# LANGUAGE FlexibleInstances     #-}
{-# LANGUAGE MultiParamTypeClasses #-}
{-# LANGUAGE NoImplicitPrelude     #-}
{-# LANGUAGE TypeFamilies          #-}
{-# LANGUAGE TypeOperators         #-}
{-# LANGUAGE UndecidableInstances  #-}

module Crypto.Alchemy.Interpreter.PTEval where

import Control.Applicative
import Crypto.Alchemy.Depth
import Crypto.Alchemy.Language.AddPT
import Crypto.Alchemy.Language.Lam
import Crypto.Alchemy.Language.Lit
import Crypto.Alchemy.Language.ModSwPT
import Crypto.Alchemy.Language.MulPT
import Crypto.Alchemy.Language.TunnelPT
import Crypto.Lol

-- | Metacircular evaluator with depth.
newtype ID (hs :: [*]) (d :: Depth) a = ID {unID :: a} deriving (Show, Eq, Functor)

-- | Metacircular plaintext symantics.
instance AddPT ID where

  type AddPubCtxPT   ID d a = (Additive a)
  type MulPubCtxPT   ID d a = (Ring a)
  type AdditiveCtxPT ID d a = (Additive a)

  a +# b = ID $ unID a + unID b
  negPT         = fmap negate
  addPublicPT a = fmap (a+)
  mulPublicPT a = fmap (a*)

instance MulPT ID where

  type RingCtxPT ID d a = (Ring a)
  type KSHintType ID d a = ()

  a *# b = ID $ unID a * unID b

instance ModSwPT ID where

  type ModSwitchCtxPT ID d (Cyc t m zp) zp' = (RescaleCyc (Cyc t) zp zp', Fact m)

  modSwitchDec = fmap rescaleDec

instance (Applicative mon) => TunnelPT mon ID where

  type TunnelCtxPT ID d t e r s zp = (e `Divides` r, e `Divides` s, CElt t zp)

  tunnelPT f = pure $ fmap (evalLin f)

-- | Metacircular lambda with depth.
instance LambdaD ID h where
  lamD f   = ID $ unID . f . ID
  appD f a = ID $ unID f $ unID a

instance Lit (ID '[] d) where
  type LitCtx (ID '[] d) a = ()
  lit = ID
